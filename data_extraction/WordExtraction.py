import PyPDF2
import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')


def extract_text_from_pdf(pdf_path, start_page=217, end_page=None):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        if end_page is None:
            end_page = len(reader.pages)-15
        for page_num in range(start_page, end_page):
            text += reader.pages[page_num].extract_text()
    return text

def extract_words(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    return words

def extract_words1(text):
        # 分析文本，提取单词部分
    lines = text.split('\n')
    words = []
    for line in lines:
        if line.strip():  # 如果行不为空
            word = line.split()[0]  # 获取每行的第一个单词
            words.append(word)
    return words

pdf_path = './file.pdf'  # 替换成你的PDF文件路径
text = extract_text_from_pdf(pdf_path)
words = extract_words1(text)

save_path = './file.txt'  # 保存提取的单词
with open(save_path, 'w') as file:
    file.write('\n'.join(words))
print(f'提取的单词已保存到 {save_path}')