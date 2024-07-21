import tools.eudic as ed

""" result = ed.add_words_to_wordbook(
    "133656375654264484", ["apple", "banana", "cherry"])
print(result)

# 示例调用
result = ed.get_words_from_wordbook("0",1,1)
print(result)


# 示例调用
result = ed.delete_wordbook("133656390109969298", "新增生词本2")
print(result)

result = ed.add_new_wordbook("新增生词本2")
print(result)

# 调用函数示例，记得替换YOUR_AUTHORIZATION_TOKEN为实际的令牌
result = ed.rename_wordbook_with_curl(
    "133656375654264484", "TOEFL", "en")
print(result)

# 调用函数示例，记
result = ed.get_wordbooks("en")
print(result) 


result = ed.delete_words_from_wordbook("133656375654264484", ["apple", "banana", "cherry"])
print(result)
 """


def read_file_add_new_words2list(file1):
    # 读取文件1和文件2的内容
    with open(file1, 'r') as f1:
        words1 = f1.read().splitlines()
        result=ed.add_words_to_wordbook(
            "", words1)
        print(result)

read_file_add_new_words2list('./data/new_words.txt')