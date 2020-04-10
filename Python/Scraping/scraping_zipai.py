import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
      


def get_page_num(url):
    num = '0'
    print('start to get %s page num'%(url))
    try:
        Result = requests.get(url, timeout=10)
        Result.encoding = Result.apparent_encoding
        html = Result.text
        num = re.findall("下一页</a> <a href='.*-(\d*).html' title='尾页'>尾页", html, re.S)[0]
        print('get page num is %s'%(num))
    except BaseException as e:
        print('错误: %s，get_page_num_err'%(str(e)))
    return int(num)


# 获取每页系列链接
def get_ser_per_page(save_dir, url, page_suffix):
    scrapy_url = url + page_suffix
    print('start to scrapy page %s'%(scrapy_url))
    ser_url = []
    try:
        Result = requests.get(scrapy_url, timeout=10)
        Result.encoding = Result.apparent_encoding
        html = Result.text
        ret = re.findall('a href="(/tupian/\d*.html)"', html, re.S)
        ser_url = [url + i for i in ret]
    except BaseException as e:
        with open(os.path.join(save_dir, 'error_download.txt'), 'a') as f:
            f.write('get_ser_per_page_err: ' + scrapy_url)
            f.write('\n')
        print('错误: %s，get_ser_per_page'%(str(e)))
    return ser_url


# 获取系列所有图片
def get_page_img_url(save_dir, url):
    print('start to scrap page %s'%(url))
    ret = []
    try:
        Result = requests.get(url, timeout=10)
        Result.encoding = Result.apparent_encoding
        html = Result.text
        ret = re.findall('data-original="(https://.*?jpg)"', html, re.S)
    except BaseException as e:
        with open(os.path.join(save_dir, 'error_download.txt'), 'a') as f:
            f.write('get_page_img_url_err: ' + url)
            f.write('\n')
        print('错误: %s，get_page_img_url'%(str(e)))
    return ret


def download_pic(save_dir, urls):
    if len(urls) > 0:
        dir_n = urls[0].split('/')[-2]
        dir_temp = os.path.join(save_dir, dir_n)
        if not os.path.exists(dir_temp):
            os.makedirs(dir_temp)
    else:
        return -1
    
    for img_url in urls:
        try:
            img_n = img_url.split('/')[-1]
            save_path = os.path.join(save_dir, dir_n, img_n)

            print('start to download img %s'%(img_url))
            pic = requests.get(img_url, timeout=10)
            fp = open(save_path, 'wb')
            fp.write(pic.content)
            fp.close()
        except BaseException as e:
            with open(os.path.join(save_dir, 'error_download.txt'), 'a') as f:
                f.write('download_pic: ' + img_url)
                f.write('\n')
            print('错误: %s，当前图片无法下载'%(str(e)))
            continue

# 为每个进程获取爬网页
def get_url_per_process(urls, num_processes = 4):
    url_list = []

    page_num = len(urls)
    if page_num < 4:
        url_list = [[i] for i in urls]
        url_list.extend([[] * (4 - page_num)])
    else:
        per_page_n = int(page_num / num_processes)
        for i in range(num_processes):
            url_list.append(urls[i * per_page_n : (i + 1) * per_page_n])
        url_list[-1] = urls[(num_processes - 1) * per_page_n : ]
    return url_list

# 进程工作
def task(url_suffix_per_page, save_dir, url):
    for i in url_suffix_per_page:
        ret = get_ser_per_page(save_dir, url, i)
        print(ret)

        ret_img_url = [get_page_img_url(save_dir, i) for i in ret]

        print(ret_img_url)

        [download_pic(save_dir, down_load_url) for down_load_url in ret_img_url]

if __name__ == '__main__':
    url = 'https://www.hhn289.com/'
    page_suffix = '/tupian/list-自拍偷拍.html'

    # url = 'https://www.hhn289.com/'
    # page_suffix = '/meinv/list-推女郎.html'
    
    save_dir = 'data'

    num = get_page_num(url + page_suffix)

    if num == 0:
        os._exit(0)
    
    # 进程数
    num_processes = 8


    url_suffix_pages = []
    # 获取网页list
    for i in range(num):
        i = i + 1
        if i != 1:
            page_suffix_finally = page_suffix.split('.html')[0] + '-' + str(i) + '.html'
        else:
            page_suffix_finally = page_suffix
        url_suffix_pages.append(page_suffix_finally)


    url_suffix_per_page = get_url_per_process(url_suffix_pages, num_processes)

    for i in url_suffix_per_page:
        print(i)

    p = Pool()
    for i in range(num_processes):
        p.apply_async(task, args = (url_suffix_per_page[i], save_dir, url,))
    p.close()
    p.join()
