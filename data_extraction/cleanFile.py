def clean_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        # 去除行首尾的空白字符
        line = line.strip()
        # 如果行为空，或者为单个'o'，或者包含非英文字符，则跳过
        if not line or line == 'o' or not line.isalpha():
            continue
        cleaned_lines.append(line)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')


# 调用函数，传入原文件路径和清理后的文件路径
clean_file('FileInput.txt', 'FileOutput.txt')
