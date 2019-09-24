import cv2
import glob
import os
import sys
from PIL import Image


def is_jpg(filename):
   try:
       i=Image.open(filename)
       return i.format =='JPEG'
   except IOError:
       return False 


def check_jpg_lists(folder):
    file_list = glob.glob(folder + '/*.jpg')

    for i in file_list:
        ret = is_jpg(i)
        #print(i, ret)

        if ret == False:
            os.remove(i)
            print('delete the jpg file: ', i)


def png2jpg(img_file):
    img = cv2.imread(img_file, 1)
    img_file = list(img_file)
    img_file[-3:] = 'jpg'
    new_file = ''.join(img_file)
    print(new_file)
    cv2.imwrite(new_file, img)


def deal_pngs(file_dir):
    # print(sys.argv[1])
    files_all = glob.glob(os.path.join(sys.argv[1], '*.png'))
    for item in files_all:
        print('delete the png file ----> ', item)
        png2jpg(item)
        os.remove(item)

if __name__ == '__main__':
    folder = sys.argv[1]
    deal_pngs(folder)
    check_jpg_lists(folder)	
