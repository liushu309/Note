### 参考
https://blog.csdn.net/weixin_43821172/article/details/105199481
### 代码 
    import shutil
    from selenium import webdriver
    import os
    import time
    import json


    # select_url = 'https://www.taobao.com'
    select_url = 'https://zc.taobao.com'
    cookie_save_dir = 'Data'
    # file_name = 'taobao_cookie.json'
    file_name = 'zc_cookie.json'

    # 1: 保存, 2: 登录
    process_index = 2


    def browser_initial_save():
        """"
        进行浏览器初始化
        """
        if not os.path.exists(cookie_save_dir):
            os.makedirs(cookie_save_dir)
        browser = webdriver.Chrome()
        log_url = select_url
        return log_url, browser


    def get_cookies_save(log_url, browser):
        """
        获取cookies保存至本地
        """
        browser.get(log_url)
        time.sleep(20)     # 进行扫码
        dictCookies = browser.get_cookies()
        jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

        with open(os.path.join(cookie_save_dir, file_name), 'w') as f:
            f.write(jsonCookies)
        print(f'{file_name} 保存成功！')
        browser.close()


    def browser_initial_login():
        """"
        进行浏览器初始化
        """
        browser = webdriver.Chrome()
        # goal_url = 'https://s.taobao.com/search?q=%E5%8D%AB%E8%A1%A3&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
        goal_url = select_url
        # 未携带cookies打开网页
        browser.get(select_url)
        return goal_url, browser


    def log_taobao_login(goal_url, browser):
        """
        从本地读取cookies并登录目标网页
        """
        # 从本地读取cookies
        with open(os.path.join(cookie_save_dir, file_name), 'r', encoding='utf8') as f:
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


    if __name__ == "__main__":
        if process_index == 1:
            tur = browser_initial_save()
            get_cookies_save(tur[0], tur[1])
        elif process_index == 2:
            tur = browser_initial_login()
            log_taobao_login(tur[0], tur[1])
