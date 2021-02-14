## 分解视频图像
可以使用如下命令：`ffmpeg -i video.mpg image-%04d.jpg`

## 编译opencv
  what():  OpenCV(3.4.4) /home/liushu/Desktop/opencv-3.4.4/modules/highgui/src/window.cpp:632: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Carbon support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'

    sudo apt-get install build-essential libgtk2.0-dev libavformat-dev libswscale-dev libavcodec-dev ffmpeg

    1. CMAKE_BUILD_TYPE                Release
    2. OPENCV_EXTRA_MODULES_PATH       contrib文件夹里的modles目录
    3. WITH_VTK 
    4. WITH_CUDA
    5. CMAKE_INSTALL_PREFIX            编译后安装位置
    7. OPENCV_GENERATE_PKGCONFIG       生成pkgconfig文件夹里的opencv.pc文件
    7. BUILD_TEST
    8. OPENCV_ENABLE_NONFREE           SIFT implementation
    9. DOPENCV_ENABLE_NONFREE
    10. BUILD_opencv_world             将所有模块编译成一个库，否则每个模块都有一个库，会很麻烦
