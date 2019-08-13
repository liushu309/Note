from PIL import Image
import glob
import os

def is_jpg(filename):
    try:
        i=Image.open(filename)
        return i.format =='JPEG'
    except IOError:
        return False 


def get_jpg_lists(folder):
    file_list = glob.glob('*.jpg')

    for i in file_list:
        file_name = os.path.join(folder, i)
        ret = is_jpg(file_name)
        print(file_name, ret)

        if ret == False:
            os.remove(file_name)
            print('delete the file: ', file_name)


'''
过滤内容不是jpg的.jpg文件
'''
if __name__ == '__main__':
    get_jpg_lists('./')	
