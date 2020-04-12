import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
from lxml import etree
import shutil
import traceback



def check_folder(path_folder):
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)
    


def get_page_num(url):
    num = '0'
    print('start to get %s page num'%(url))
    try:
        Result = requests.get(url, timeout=20)
        Result.encoding = Result.apparent_encoding
        html = Result.text
        num = re.findall("下一页</a> <a href='.*-(\d*).html' title='尾页'>尾页", html, re.S)[0]
        print('get page num is %s'%(num))
    except BaseException as e:
        traceback.print_exc()
        print('错误: %s，get_page_num_err'%(str(e)))
    return int(num)


# 获取每页系列链接
def get_ser_per_page(save_dir, url, page_suffix):
    scrapy_url = url + page_suffix
    print('start to scrapy page %s'%(scrapy_url))
    ser_url = []
    try:
        Result = requests.get(scrapy_url, timeout=20)
        Result.encoding = Result.apparent_encoding
        html = Result.text
        soup = BeautifulSoup(html, "html.parser")
        ret = soup.find_all(lambda tag:tag.name == 'a' and len(tag.contents) > 1 and tag.has_attr('title'))
        ser_url = [url + i.get('href') for i in ret]
    except BaseException as e:
        traceback.print_exc()
        check_folder(save_dir)
        write_f_n = os.path.join(save_dir, 'error_download.txt')
        with open(write_f_n, 'a', encoding='utf-8') as f:
            f.write('get_ser_per_page_err: ' + scrapy_url)
            f.write('\n')
        print('错误: %s，get_ser_per_page'%(str(e)))
    return ser_url


# 获取系列所有图片
def get_page_img_url(save_dir, url, download_flag):
    print('start to scrap page %s'%(url))
    ret = []
    info_list = [[]]
    try:
        Result = requests.get(url, timeout=20)
        Result.encoding = Result.apparent_encoding
        html = Result.text
        if download_flag == 0:
            # 获取jpg
            # ret = re.findall('data-original="(https://.*?jpg)"', html, re.S)
            # 获取jpg, 获取标题
            so_ret = BeautifulSoup(html, "html.parser")
            ret = so_ret.find_all(lambda tag:tag.name == 'img' and tag.has_attr('title'))
            info_list=[[i.get('data-original').strip(), i.get('title')] for i in ret]
        else:
            info_list = []
            html = etree.HTML(html)
            info_list.append(html.xpath('//input/@data-clipboard-text'))

    except Exception as e:
        traceback.print_exc()
        check_folder(save_dir)
        write_f_n = os.path.join(save_dir, 'error_download.txt')
        with open(write_f_n, 'a', encoding='utf-8') as f:
            f.write('get_page_img_url_err: ' + url)
            f.write('\n')
        print('错误: %s，get_page_img_url'%(str(e)))
    return info_list


def download_pic(save_dir, urls, download_flag):
    if download_flag == 0:
        if len(urls) > 0:
            dir_temp = os.path.join(save_dir, urls[0][1])
            if not os.path.exists(dir_temp):
                os.makedirs(dir_temp)
        else:
            return -1
        
        for img_url_l in urls:
            try:
                img_url = img_url_l[0]
                img_n = img_url.split('/')[-1]
                save_path = os.path.join(dir_temp, img_n)

                print('start to download img %s'%(img_url))
                pic = requests.get(img_url, timeout=20)
                fp = open(save_path, 'wb')
                fp.write(pic.content)
                fp.close()
            except Exception as e:
                traceback.print_exc()
                check_folder(save_dir)
                write_f_n = os.path.join(save_dir, 'error_download.txt')
                with open(write_f_n, 'a', encoding='utf-8') as f:
                    f.write('download_pic: ' + img_url)
                    f.write('\n')
                print('错误: %s，当前图片无法下载'%(str(e)))
                continue
    elif download_flag == 1:
        if len(urls) > 0:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
        try:
            save_path_normal = os.path.join(save_dir, 'normal.txt')
            save_path_thunder = os.path.join(save_dir, 'thunder.txt')

            print('start to download video path %s'%(save_path_thunder))
            fp = open(save_path_normal, 'a', encoding='utf-8')
            fp.write(urls[0][0])
            fp.write('\n')
            fp.close()
            fp = open(save_path_thunder, 'a', encoding='utf-8')
            fp.write(urls[0][1])
            fp.write('\n')
            fp.close()
        except Exception as e:
            traceback.print_exc()
            check_folder(save_dir)
            write_f_n = os.path.join(save_dir, 'error_download.txt')
            with open(write_f_n, 'a', encoding='utf-8') as f:
                print('-------------------->\n',urls[0][0])
                f.write('download_pic: ' + urls[0][0])
                f.write('\n')
            print('错误: %s，无法保存网页'%(str(e)))


# 为每个进程获取爬网页
def get_url_per_process(urls, num_processes = 4):
    url_list = []

    page_num = len(urls)
    if page_num < num_processes:
        url_list = [[i] for i in urls]
        url_list.extend([[] * (num_processes - page_num)])
    else:
        per_page_n = int(page_num / num_processes)
        for i in range(num_processes):
            url_list.append(urls[i * per_page_n : (i + 1) * per_page_n])
        if per_page_n * num_processes < page_num:
            rest_urls = page_num - per_page_n * num_processes
            for i in range(rest_urls):
                url_list[i].append(urls[per_page_n * num_processes + i])
    return url_list

# 进程工作
def task(url_suffix_per_page, save_dir, url, download_flag):
    for i in url_suffix_per_page:
        try:
            ret = get_ser_per_page(save_dir, url, i)
            print(ret)

            ret_img_url_title = [get_page_img_url(save_dir, i, download_flag) for i in ret]

            print(ret_img_url_title[0][0][0])

            [download_pic(save_dir, down_load_url, download_flag) for down_load_url in ret_img_url_title]
        except Exception as e:
            print('error: ' + str(e))
            traceback.print_exc()

def main_work(url, page_suffix_list, save_dir, num_processes, download_flag):
    for page_suffix in page_suffix_list:

        dir_temp = page_suffix.split('list-')[1].split('.html')[0]
        save_dir_suffix = os.path.join(save_dir, dir_temp)

        num = get_page_num(url + page_suffix)

        if num == 0:
            os._exit(0)

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
            p.apply_async(task, args = (url_suffix_per_page[i], save_dir_suffix, url,download_flag,))
        p.close()
        p.join()



if __name__ == '__main__':
    url = 'https://www.hhx682.com'

    page_suffix = ['/tupian/list-自拍偷拍.html']
    # xiezhen_list = ['/meinv/list-推女郎.html', '/meinv/list-头条女神.html', '/meinv/list-3Agirl写真.html', '/meinv/list-推女神.html', '/meinv/list-爱蜜社.html', '/meinv/list-美媛馆新刊.html', '/meinv/list-秀人网.html', '/meinv/list-波萝社.html', '/meinv/list-优星馆.html', '/meinv/list-Pantyhose.html', '/meinv/list-假面女皇.html', '/meinv/list-嗲囡囡.html', '/meinv/list-模范学院.html', '/meinv/list-魅妍社.html', '/meinv/list-V女郎.html', '/meinv/list-兔宝宝.html']
    xiezhen_list = ['/meinv/list-3Agirl写真.html', '/meinv/list-爱蜜社.html', '/meinv/list-美媛馆新刊.html', '/meinv/list-秀人网.html', '/meinv/list-波萝社.html', '/meinv/list-优星馆.html', '/meinv/list-Pantyhose.html', '/meinv/list-假面女皇.html', '/meinv/list-嗲囡囡.html', '/meinv/list-模范学院.html', '/meinv/list-魅妍社.html', '/meinv/list-V女郎.html', '/meinv/list-兔宝宝.html']

    video_list = ['/xiazai/list-亚洲电影.html', '/xiazai/list-欧美电影.html', '/xiazai/list-制服丝袜.html', '/xiazai/list-强奸乱伦.html', '/xiazai/list-国产自拍.html', '/xiazai/list-变态另类.html', '/xiazai/list-经典三级.html', '/xiazai/list-成人动漫.html']

    # video_list = ['/xiazai/list-经典三级.html']

    save_dir = 'data'

    # 进程数
    num_processes = 8

    # 0 图片, 1 磁力连接
    download_flag = 0

    main_work(url, xiezhen_list, save_dir, num_processes, download_flag)

