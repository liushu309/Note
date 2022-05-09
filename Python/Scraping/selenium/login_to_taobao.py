# 淘宝网的代码跟大麦的大致相同，唯一不同的就是大麦网在登录页面刷新操作后就显示已登录状态了，而淘宝网刷新没用，必须新打开网页才行。所以淘宝网必须先打开一次用于登录，然后再打开目标网页。


from selenium import webdriver
import os
import json
import time

def browser_initial():
    """"
    进行浏览器初始化
    """
    os.chdir('E:\\pythonwork')
    browser = webdriver.Chrome()
    goal_url = 'https://s.taobao.com/search?q=%E5%8D%AB%E8%A1%A3&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
    # 未携带cookies打开网页
    browser.get('https://www.taobao.com/')
    return goal_url,browser

def log_taobao(goal_url,browser):
    """
    从本地读取cookies并登录目标网页
    """
    # 从本地读取cookies
    with open('taobao_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())

    for cookie in listCookies:
        cookie_dict = {
            'domain': '.taobao.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'path': '/',
            "expires": '',
            'sameSite': 'None',
            'secure': cookie.get('secure')
        }
        browser.add_cookie(cookie_dict)

    # 更新cookies后进入目标网页
    browser.get(goal_url)

if __name__ == '__main__':
    tur = browser_initial()
    log_taobao(tur[0],tur[1])
