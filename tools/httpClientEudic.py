import http.client


def fetch_studylist_category(language='en'):
    """
    获取指定语言的生词本分类列表。

    :param language: 查询的语言，默认为英语（'en'）
    :return: 生词本分类列表的JSON字符串
    """
    conn = http.client.HTTPSConnection("api.frdic.com")
    payload = ''
    headers = {
        'Authorization': ''
    }
    conn.request("GET", f"/api/open/v1/studylist/category?language={language}",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    return data.decode("utf-8")


# 示例调用
print(fetch_studylist_category('en'))
