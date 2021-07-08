## 1. 安装MinGW
一定要是64位的，不然出现什么Thread, posix, win32之类的

## 2. CMakeLists.txt
    cmake_minimum_required(VERSION 3.9.1)
    set(CMAKE_C_COMPILER "gcc")#设置C编译器
    set(CMAKE_C_FLAGS "-g -Wall  -I D:/SoftWare/Mingw64/include -L D:/SoftWare/Mingw64/lib")#

    set(CMAKE_CXX_COMPILER "g++")#设置C++编译器
    set(CMAKE_CXX_FLAGS "-g -Wall  -I D:/SoftWare/Mingw64/include -L D:/SoftWare/Mingw64/lib")

    set(CMAKE_SH "CMAKE_SH-NOTFOUND")

    project(demo)

    set(OpenCV_DIR "D:/SoftWare/OpenCV_3.4.15")
    find_package(OpenCV REQUIRED)
    include_directories(${OpenCV_INCLUDE_DIRS})
    
    add_executable(demo opencv.cpp)
    target_link_libraries(demo ${OpenCV_LIBS})
    
## 3. 编译指令
    cmake -G "MinGW Makefiles" ..
    mingw32-make
