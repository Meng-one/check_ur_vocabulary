from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from tools import eudic as ed

app = Flask(__name__)
app.secret_key = ''

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# 假设的用户存储
users = {'admin': {'password': generate_password_hash('')}}

# 加载单词列表


def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


words = load_words('merged_sorted.txt')
new_words = []
current_index = 0


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return None
    user = User()
    user.id = username
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password'], password):
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    global current_index
    if current_index < len(words):
        word = words[current_index]
        return render_template('index.html', word=word, progress=f"{current_index + 1}/{len(words)}", new_words_count=len(new_words), new_words_list=new_words)
    else:
        return render_template('complete.html')


@app.route('/mark_new_word/<word>')
def mark_new_word(word):
    new_words.append(word)
    return redirect(url_for('next_word'))


@app.route('/next_word')
def next_word():
    global current_index
    current_index += 1
    return redirect(url_for('index'))


@app.route('/upload_words', methods=['POST'])
def upload_words():
    if new_words:
        result = ed.add_words_to_wordbook("133656375654264484", new_words)
        print(result)
        # 假设 save_progress 函数已定义
        # save_progress()
        return "新单词已上传到生词本"
    else:
        return "没有新单词需要上传"


if __name__ == "__main__":
    app.run(debug=True)
