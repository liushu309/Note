## 1. 分解视频图像
可以使用如下命令：`ffmpeg -i video.mpg image-%04d.jpg`

## 2. 编译opencv
### 2.1以opencv4.5.1为例
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
   
### 2.2 常见问题
  1. 出现fatal error: boostdesc_bgm.i: No such file or directory
将百度网盘里的文件boostdesc_bgm.i,vgg_generated_48.i等.rar解压后，放在 opencv_contrib/modules/xfeatures2d/src/ 路径下即可

  2. fatal error: features2d/test/test_detectors_regression.impl.hpp: No such file or directory
原因是没找到这个文件
将opencv / modules / features2d复制，然后粘贴到build目录中来解决该问题。 


## 3. 在Ubuntu上配置环境
### 3.1 配置pkg
    $ sudo vim /etc/profile
    # 添加字段，这里一定要加上export，不加只是配置了PKG_CONFIG_PATH这个变量，加了才加入到了系统里
    export  PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/opencv4/lib/pkgconfig 
    # 更新配置
    $ source ~/.bashrc
### 3.2 库添加到路径
    $ sudo gedit /etc/ld.so.conf.d/opencv.conf 
    # 在文件中写入
    /usr/local/opencv4/lib  
    $ sudo ldconfig  

### 3.3 测试

    #include <opencv2/opencv.hpp>
    #include <iostream>

    using namespace cv;

    int main(){
      Mat a = cv::imread("./1.jpg", 1);
      imshow("test", a);
      waitKey(0);
      return 0;
    }
    # 注意，g++后面跟文件名，不要把文件放在最后，容易报错
    $ g++ test1.cpp `pkg-config opencv4 --libs --cflags` -o app

### 3.4 在vscode上配置环境
在vscode上运行上面的代码  
c_cpp_properties.json文件  

    {
        "configurations": [
            {
                "name": "Linux",
                "includePath": [
                    "${workspaceFolder}/**",
                    // 只修改了这一行
                    "/usr/local/opencv_4.5.1/include/opencv4"  
                ],
                "defines": [],
                "compilerPath": "/usr/bin/gcc",
                "cStandard": "gnu17",
                "cppStandard": "gnu++14",
                "intelliSenseMode": "linux-gcc-x64"
            }
        ],
        "version": 4
    }

tasks.json文件

    {
        "tasks": [
            {
                "type": "cppbuild",
                "label": "C/C++: g++ 生成活动文件",
                "command": "/usr/bin/g++",
                "args": [
                    "-g",
                    "${file}",
                    "-o",
                    "${fileDirname}/${fileBasenameNoExtension}", 
                    // 只添加了下面这三行，注意，“－l”和“opencv_world”不能简写成"lopencv_world",以及前面不要加lib,如libopencv_world
                    "-I", "/usr/local/opencv_4.5.1/include/opencv4",
                    "-L", "/usr/local/opencv_4.5.1/lib",
                    "-l", "opencv_world"
                ],
                "options": {
                    "cwd": "${workspaceFolder}"
                },
                "problemMatcher": [
                    "$gcc"
                ],
                "group": {
                    "kind": "build",
                    "isDefault": true
                },
                "detail": "调试器生成的任务。"
            }
        ],
        "version": "2.0.0"
    }