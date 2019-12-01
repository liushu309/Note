import os
import cv2
import glob
from PIL import Image

def jpg2video_zh_test(img_path, video_save_path, fps):
    """ 将图片合成视频. video_save_path: 视频路径，fps: 帧率 """
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    images = glob.glob(os.path.join(img_path, '*.jpg'))
    images.sort()
    print('len(images)--------> ', len(images))
    image = Image.open(images[0])
    vw = cv2.VideoWriter(video_save_path, fourcc, fps, image.size)
    for jpgfile in images:
        try:
            frame = cv2.imread(jpgfile)
            vw.write(frame)
        except Exception as exc:
            print(jpgfile, exc)
    vw.release()


if __name__ == '__main__':
    jpg2video_zh_test('data/image', 'liushu.avi', 20)
