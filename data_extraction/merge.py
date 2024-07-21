# 定义合并和排序单词的函数
def merge_and_sort_files(file1, file2, output_file):
    # 读取文件1和文件2的内容
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        words1 = f1.read().splitlines()
        words2 = f2.read().splitlines()

    # 合并两个列表并去除重复的单词
    unique_words = set(words1 + words2)

    # 将集合转换回列表并排序
    sorted_words = sorted(list(unique_words))

    # 将排序后的单词写入到新文件中
    with open(output_file, 'w') as f_out:
        for word in sorted_words:
            f_out.write(word + '\n')




