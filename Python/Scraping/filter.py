from PIL import Image
import glob
import os
import sys

def is_jpg(filename):
    try:
        i=Image.open(filename)
        return i.format =='JPEG'
    except IOError:
        return False 


def get_jpg_lists(folder):
    file_list = glob.glob(folder + '/*.jpg')

    for i in file_list:
        ret = is_jpg(i)
        print(i, ret)

        if ret == False:
            os.remove(i)
            print('delete the file: ', i)

if __name__ == '__main__':
    folder = sys.argv[1]
    get_jpg_lists(folder)	
