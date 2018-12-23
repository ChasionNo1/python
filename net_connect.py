import requests
import base64


def check_net():
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
    try:
        response = requests.get(url=url, headers=headers)
        if '百度一下' in response.content.decode():
            return '网络已经连接'
    except requests.exceptions.ConnectionError:
        return '网络没有连接'

