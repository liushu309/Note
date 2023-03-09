## 1. CMake使用

### 1.1 cmake常见查找库

    # 查看库所在路径
    dpkg -L 库名
    # whereis
    whereis 库名
    # 推荐查找方式（）
    locate 库名
    # 第一种，查找单一库文件
    # find_library(JSONCPP（自定义名） NAMES（可以取的名字flag） jsoncpp(可能取的名字)
    #              HINTS（可能存在的路径） /usr/lib/x86_64-linux-gnu)
    include_directories(/usr/include/jsoncpp)
    # 通配符查找很多的库
    file(GLOB(通配符flag) JSON_LIB(自定义名称) "/usr/lib/x86_64-linux-gnu/*.so")
    # 例如
    FILE(GLOB PJSIP_LIB "/usr/local/PJSip/lib/*.a")
    
 ### 1.2cmake动静库链接方式的不同
 
    # 动态库链接
    file(GLOB opencv_lib "/usr/local/opencv/lib/*.so")
    target_link_libaries(${PROJECT_NAME} opencv_lib)
    
    # 静态库链接
    # 动态库的链接不能使用上面的方式进行，因为target_link_libaries(target object), 其中object如果不是-lXXX的形式，可能会被cmake认为是自定义的生成目标，file方式获取来的库目录都是路径加上库的名称，之间使用分号进行分隔，可能会被cmake认为是一个库的，所以无法链接，所以使用最为通常的方式
    target_link_libries(${PROJECT_NAME} -lopencv_core -lopencv_huixx ...)
 


