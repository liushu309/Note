    =================================== 简明 =================================
    创建build文件，cd build, cmake .., make, ./hello
    ├── 1.jpeg
    ├── build
    ├── CMakeLists.txt
    ├── main.cpp
    └── mymath
        ├── add_func.cpp
        ├── add_func.h
        └── CMakeLists.txt

    cmake_minimum_required(VERSION 3.16)
    # 工程名称
    project(liushu)
    # 自己开发的库目录
    add_subdirectory(mymath)
    # opencv头文件目录（自己开发的库目录，在add_subdirectory后不需要在CMakeLists.txt文件中配置include path）
    include_directories(/usr/local/OpenCV/OpenCV-3.4.15/include)
    # 使用正则表达式”...*.so“来匹配特定目录下，所有名称中以.so结尾的文件（动态链接库格式）的文件名称（包含绝对路径），将基放入自定义变量OPENCV_LIB中
    FILE(GLOB OPENCV_LIB "/usr/local/OpenCV/OpenCV-3.4.15/lib/*.so")
    # 生成可执行文件hello
    add_executable(hello main.cpp)
    # 将可执行文件hello和所有库文件进行链接
    target_link_libraries(hello mymath ${OPENCV_LIB})

    # ======================= mymath 文件中的CMakeLists.txt===========================
    # add_library(mymath add_func.cpp)  



    # ========================== 详细教程 =======================================
    ├── CMakeLists.txt
    ├── COPYRIGHT
    ├── doc
    │   └── hello.txt
    ├── main.cpp
    ├── mymath
    │   ├── CMakeLists.txt
    │   ├── myadd.cpp
    │   └── myadd.h
    ├── mymath2
    │   ├── CMakeLists.txt
    │   ├── mymul.cpp
    │   └── mymul.h
    ├── README.md
    └── runhello.sh

    
    cmake_minimum_required(VERSION 3.9)

    # 在原文件目录下新建一个新的文件夹，比如build，进目录，再运行“cmake ..”命令

    # project命令隐式定义了两个CMAKE的变量
    # xxx_BINARY_DIR，本例中是 liushu_BINARY_DIR
    # xxx_SOURCE_DIR，本例中是 liushu_SOURCE_DIR
    project(liushu)
    message(STATUS "构建目录，build目录" ${liushu_BINARY_DIR})
    message(STATUS "源代码主目录，主CMakeLists.txt目录" ${liushu_SOURCE_DIR})
    # -- 构建目录，build目录               /home/liushu/Documents/Projects/C++/Test_02/build
    # -- 源代码主目录，主CMakeLists.txt目录/home/liushu/Documents/Projects/C++/Test_02


    # 设置动态库和静态库的编译输出路径，如build/lib，不是安装路径，这个必须是在下面介绍的add_subdirectory前面，不然不起作用
    set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
    # 指定最终的主程序⼆进制的位置，可以放在最后
    set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin) 

    # bin1和bin2替换构建目录下的子目录名称，如果不加这个名称，则目录名称为mymath, mymath2
    # build
    # ├── bin1(之前的名称为"mymath")
    # │...
    # │   ├── libmyadd.so
    # │   └── Makefile
    # ├── bin2
    # │...
    # │   ├── libmymul.a
    # │   └── Makefile
    add_subdirectory(./mymath bin1)
    add_subdirectory(./mymath2 bin2)

    include_directories("./mymath")
    include_directories("./mymath2")

    add_executable(foo main.cpp)

    target_link_libraries(foo myadd mymul)

    # 安装路径前缀
    set(CMAKE_INSTALL_PREFIX ${liushu_BINARY_DIR}/install)
    # 安装单个文件
    install(FILES COPYRIGHT runhello.sh README.md DESTINATION ${CMAKE_INSTALL_PREFIX})
    # 安装文件夹及包含文件
    install(DIRECTORY doc DESTINATION ${CMAKE_INSTALL_PREFIX})

    # 头文件
    install(FILES mymath/myadd.h mymath2/mymul.h DESTINATION ${CMAKE_INSTALL_PREFIX}/include)

    # 注意，因为可执行二进制文件和库文件由于名称有变化（如上面写的库名称为myadd，而实际加版本号生成的库文件名称为libmyadd.so.1.2，文件也可能不止一个，比如还可能有libadd.so.1）,以及构建输出目录有设置（如set(LIBRARY_OUTPUT_PATH path_to_your_setting)）,所以这里使用TARGETS进行统一管理和安装
    # ⼆进制，静态库，动态库安装都⽤TARGETS
    # ARCHIVE 特指静态库
    # LIBRARY 特指动态库
    install(TARGETS myadd mymul LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)
    # RUNTIME 特指可执⾏⽬标⼆进制。
    install(TARGETS foo RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)


    # ==================== mamath CMakeLists.txt =======================
    # 找到当前目录下的所有源文件，赋值给 SRC_FILES
    aux_source_directory(. SRC_FILES)
    # 生成动态库（静态库改为STATIC），不加SHARED默认生态静态库
    add_library(myadd SHARED ${SRC_FILES})
    # 设置版本号(VERSION 1.2会形成一个libmyadd.so.1.2的文件或快捷方式，SOVERSION 1会开成一个libmyadd.so.1的文件或快捷方式,所以两个都要写
    # lrwxrwxrwx 1 liushu liushu   13 3月   5 19:41 libmyadd.so -> libmyadd.so.1
    # lrwxrwxrwx 1 liushu liushu   15 3月   5 19:41 libmyadd.so.1 -> libmyadd.so.1.2
    # -rwxrwxr-x 1 liushu liushu  16K 3月   5 19:41 libmyadd.so.1.2
    set_target_properties(myadd PROPERTIES VERSION 1.2 SOVERSION 1)

    # ==================== mamath2 CMakeLists.txt =======================
    aux_source_directory(. SRC_FILES)
    add_library(mymul STATIC ${SRC_FILES})
