import subprocess
import json

My_authorization_token = ""


def get_wordbooks(language="en"):
    """
    使用curl命令获取所有生词本信息

    :param language: 生词本的语言
    :return: 生词本信息的JSON对象
    """
    curl_command = f"""curl --location --request GET 'https://api.frdic.com/api/open/v1/studylist/category?language={language}' \
--header 'Authorization: {My_authorization_token}'"""

    process = subprocess.Popen(
        curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return json.loads(stdout)
    else:
        print(f"Error executing curl command: {stderr}")
        return None
    

def rename_wordbook_with_curl(wordbook_id, new_name, language="en"):
    """
    使用curl命令重命名一个生词本

    :param wordbook_id: 生词本的ID
    :param new_name: 新的生词本名称
    :param language: 生词本的语言，默认为英语
    :param authorization_token: 认证令牌
    :return: curl命令的输出
    """
    curl_command = f"""curl --location --request PATCH 'https://api.frdic.com/api/open/v1/studylist/category' \
--header 'Authorization: {My_authorization_token}' \
--header 'Content-Type: application/json' \
--data-raw '{{
    "id": "{wordbook_id}",
    "language": "{language}",
    "name": "{new_name}"
}}'"""

    process = subprocess.Popen(
        curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if process.returncode == 0:
        return json.loads(output.decode('utf-8'))
    else:
        return {"error": error.decode('utf-8')}


def add_new_wordbook(name,language="en"):
    """
    使用curl命令添加一个新的生词本

    :param language: 生词本的语言
    :param name: 生词本的名称
    :return: 新生词本信息的JSON对象
    """
    curl_command = f"""curl --location --request POST 'https://api.frdic.com/api/open/v1/studylist/category' \\
--header 'Authorization: {My_authorization_token}' \\
--header 'Content-Type: application/json' \\
--data-raw '{{
    "language": "{language}",
    "name": "{name}"
}}'"""

    process = subprocess.Popen(
        curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return json.loads(stdout)
    else:
        print(f"Error executing curl command: {stderr}")
        return None


def delete_wordbook(wordbook_id,  name,language="en"):
    """
    使用curl命令删除一个生词本

    :param wordbook_id: 生词本的ID
    :param language: 生词本的语言
    :param name: 生词本的名称
    :return: 操作结果的提示信息
    """
    curl_command = f"""curl --location --request DELETE 'https://api.frdic.com/api/open/v1/studylist/category' \\
--header 'Authorization: {My_authorization_token}' \\
--header 'Content-Type: application/json' \\
--data-raw '{{
    "id": "{wordbook_id}",
    "language": "{language}",
    "name": "{name}"
}}'"""

    process = subprocess.Popen(
        curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return "删除成功"
    else:
        print(f"Error executing curl command: {stderr}")
        return "删除失败"


def get_words_from_wordbook(wordbook_id, page=1, page_size=100, language="en",):
    """
    使用curl命令获取指定生词本中的单词列表

    :param wordbook_id: 生词本的ID
    :param language: 生词本的语言，默认为英语（'en'）
    :param page: 分页页数，默认为1
    :param page_size: 分页单词数量，默认为100
    :return: 生词本中单词的JSON对象
    """
    curl_command = f"""curl --location --request GET 'https://api.frdic.com/api/open/v1/studylist/words/{wordbook_id}?language={language}&page={page}&page_size={page_size}' \
--header 'Authorization: {My_authorization_token}'"""

    process = subprocess.Popen(
        curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return json.loads(stdout.decode('utf-8'))
    else:
        print("Error:", stderr.decode('utf-8'))
        return None


def add_words_to_wordbook(wordbook_id, words, language="en"):
    """
    往生词本里添加单词的函数

    :param wordbook_id: 生词本的ID
    :param words: 单词数组
    :param language: 语言，默认为英语（'en'）
    :return: 操作结果的提示信息
    """

    # 构造请求体
    data = {
        "id": wordbook_id,
        "language": language,
        "words": words
    }
    data_json = json.dumps(data)

    # 构造curl命令
    curl_command = f"""curl --location --request POST 'https://api.frdic.com/api/open/v1/studylist/words' \\
--header 'Authorization: {My_authorization_token}' \\
--header 'Content-Type: application/json' \\
--data-raw '{data_json}'"""

    # 执行curl命令
    process = subprocess.Popen(
        curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # 处理响应
    if process.returncode == 0:
        return json.loads(stdout.decode('utf-8'))
    else:
        print(f"Error executing curl command: {stderr.decode('utf-8')}")
        return None


def delete_words_from_wordbook(wordbook_id, words, language="en"):
    """
    使用curl命令删除生词本中的单词

    :param wordbook_id: 生词本的ID
    :param words: 要删除的单词数组
    :param language: 生词本的语言
    :return: 操作结果的提示信息
    """
    data = {
        "id": wordbook_id,
        "language": language,
        "words": words
    }
    data_json = json.dumps(data)

    curl_command = f"""curl --location --request DELETE 'https://api.frdic.com/api/open/v1/studylist/words?language={language}&category_id={wordbook_id}' \
--header 'Authorization: {My_authorization_token}' \
--header 'Content-Type: application/json' \
--data-raw '{data_json}'"""

    process = subprocess.Popen(
        curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return {"message": "单词删除成功"}
    else:
        return {"message": f"删除失败，错误信息: {stderr.decode('utf-8')}"}
