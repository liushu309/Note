## 1. CMake使用

### 1.1 cmake常见查找库

    # 查看库所在路径
    dpkg -L 库名
    # 第一种，查找单一库文件
    # find_library(JSONCPP（自定义名） NAMES（可以取的名字flag） jsoncpp(可能取的名字)
    #              HINTS（可能存在的路径） /usr/lib/x86_64-linux-gnu)
    include_directories(/usr/include/jsoncpp)
    # 通配符查找很多的库
    file(GLOB(通配符flag) JSON_LIB(自定义名称) "/usr/lib/x86_64-linux-gnu/*.so")
