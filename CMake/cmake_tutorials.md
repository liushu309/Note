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
