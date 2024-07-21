import tkinter as tk
from tkinter import ttk
from tools import eudic as ed

class VocabularyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("生词本")
        self.root.geometry("400x200")

        self.words = self.load_words('merged_sorted.txt')
        self.new_words = []
        self.current_index = 0

        self.create_widgets()
        self.next_word()

    def load_words(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def is_new_word(self, new_word):
        self.new_words.append(new_word)
        self.next_word()


    def not_new_word(self):
        self.next_word()


    def next_word(self):
        if self.current_index < len(self.words):
            word = self.words[self.current_index]
            self.word_label.config(text=word)
            self.current_index += 1
        else:
            self.word_label.config(text="完成！")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
        self.update_progress()

    def save_progress(self):
        with open('merged_sorted.txt', 'w') as file:
            for word in self.words[self.current_index-1:]:
                file.write(word + '\n')

    def save_new_words(self):
        with open('new_words.txt', 'a') as file:
            for word in self.new_words:
                file.write(word + '\n')

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=10)

        self.progress_label = ttk.Label(self.root, font=("Arial", 12))
        self.progress_label.pack()

        self.word_label = ttk.Label(self.root, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.yes_button = ttk.Button(self.button_frame, text="认识",
                                     command=self.not_new_word, width=20)
        self.yes_button.pack(side=tk.TOP, padx=10)

        self.no_button = ttk.Button(self.button_frame, text="不认识",
                                    command=lambda: self.is_new_word(self.word_label['text']), width=20)
        self.no_button.pack(side=tk.TOP, padx=10)
        
        self.regret_button = ttk.Button(self.button_frame, text="撤销",command=self.regret, width=20)
        self.regret_button.pack(side=tk.TOP, padx=10)


    def regret(self):
        word = self.words[self.current_index-1]
        self.word_label.config(text=word)
        self.current_index -= 1
        self.update_progress()
    
    def update_progress(self):
        self.progress_label.config(
            text=f"{self.current_index}/{len(self.words)}")


    def upload_words(self):
            # 假设TestEudic模块已经被导入，并且有一个add_words_to_wordbook方法
            # 这里我们调用这个方法来上传单词
            # 注意：这里需要根据TestEudic的实际实现来调整参数
            if self.new_words:  # 如果有新单词需要上传
                result=ed.add_words_to_wordbook("133656375654264484",self.new_words)
                print(result)
                print("新单词已上传到生词本")
            else:
                print("没有新单词需要上传")

    def on_closing(self):
        self.save_new_words()
        self.save_progress()
        self.upload_words()  # 调用上传单词的方法
        self.root.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = VocabularyApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
