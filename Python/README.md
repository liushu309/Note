## python加入包路径
### 1. 在包路径下创建文件
    __init__.py
### 2. 在里面复制以下代码
    import os
    import sys

    rootpath = str(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(rootpath)
    
## 3. python “...”操作符
在Python中，“...”(ellipsis)操作符，表示其他维度不变，只操作最前或最后1维

    import numpy as np
    
    x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    """[[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12]]"""
    print(x.shape)  # (3, 4)
    y = x[1:2, ...]
    """[[5 6 7 8]]"""
    print(y)

## 4. python "::-1"
“::-1”是颠倒数组的值，例如：  

    import numpy as np

    a = np.array([1, 2, 3, 4, 5])
    print a[::-1]
    """[5 4 3 2 1]"""

## 5. @classmethod和@staticmethod
### @classmethod    
   1. classmethod 是一个装饰器函数，用来标示一个方法为类方法    
   2. 类方法的第一个参数是类对象参数，在方法被调用的时候自动将类对象传入，参数名称约定为cls  
   3. 如果一个方法被标示为类方法，则该方法可被类对象调用(如 C.f())，也可以被类的实例对象调用(如 C().f())  
   4. 类被继承后，子类也可以调用父类的类方法，但是第一个参数传入的是子类的类对象    
   5. 可以访问和类相关（不和实例相关)的属性，看 test.my_class_print("class print") 和 my_test.my_class_print("class print") 的结果都是class中定义的class_name  的值，非实例的值：xxx 

### @staticmethod    
   1. Class methods are different than C++ or Java static methods. If you want those, see staticmethod() in this section.  
   2. 不需要访问和类相关的属性或数据(感觉只是概念上的区别，你这样声明了用的人就知道了，如果你非要在这个方法中访问test.xxx 它就和@classmethod的作用一样了。）
   
## 6. __dict__()
对象的__dict__()和类的__dict__()方法不同,对象的只是对象的属性,类的还有一些其它的信息    

    class A:
        some = 1
        def __init__(self,num):
            self.num = num
    a = A(10)

    print(a.__dict__)
    #out {'num': 10}
    a.liushu = 10
    print(a.__dict__)
    #out {'num': 10, 'liushu': 10}
    print(A.__dict__)
    #out {'__module__': '__main__', 'some': 1, '__init__': <function A.__init__ at 0x7f066a86a1e0>, '__dict__': <attribute '__dict__' of 'A' objects>,'__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

## 7.map
map() 会根据提供的函数对指定序列做映射。  
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。  

    map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    out:
    [3, 7, 11, 15, 19]
    
## 8. trackback
在python多层调用或者需要将错误信息提到出来进行输出的时候，可以使用traceback  

    import sys
    import time
    import traceback

    def func(a, b):
        return a / b

    if __name__ == '__main__':
        try:
            func(1, 0)
        except Exception as e:
            print('***', type(e), e, '***')
            time.sleep(2)

            print("***traceback.print_exc():*** ")
            time.sleep(1)
            traceback.print_exc()
            time.sleep(2)

            print("***traceback.format_exc():*** ")
            time.sleep(1)
            print(traceback.format_exc())
            time.sleep(2)

            print("***traceback.print_exception():*** ")
            time.sleep(1)
            traceback.print_exception(*sys.exc_info())
## 9. python调用shell
    import subprocess
    ret = subprocess.Popen('ping www.baidu.com -c 3', stdout = subprocess.PIPE, shell = True)
    for i in ret.stdout:
        print(i)

## 10. python调用ffmpeg对视频进行填充缩放
先检测数据完整性

    def check_video(file_name):
        try:
            # 执行probe执行
            probe = ffmpeg.probe(file_name)
            video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            return video_stream
        except Exception as e:
            print(e)
            return None



-vf video_fileter  
-i input  

    input_name = '3.mp4'
    out_name = '3_224.mp4'
    ret = subprocess.Popen('ffmpeg -i  {0} -vf "scale = iw*min(224/iw\, 224/ih):ih*min(224/iw\, 224/ih), pad=224:224:(224-iw*min(224/iw\, 224/ih))/2\:(224-ih*min(224/iw\, 224/ih))/2:black" {1}'.format(input_name, out_name), stdout = subprocess.PIPE, shell = True).communicate() 
    cap = cv2.VideoCapture('3_224.mp4')
    ret = True
    while ret:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('test', frame)
            cv2.waitKey(10)


## 11. python调用C++函数/类
有三种方式:  
1. ctype(只能调用函数,不能调用类)  
2. boost_python(编译复杂)  
3. pybind11(简单,可调用类)  

pip install pybind11  
教程: https://zhuanlan.zhihu.com/p/80884925  

    #include <pybind11/pybind11.h>
    #include <iostream>
    using namespace std;
    class Hello
    {
    public:
        Hello() {}
        void say(const std::string s)
        {
            std::cout << s << std::endl;
        }
    };

    PYBIND11_MODULE(py2cpp, m)
    {
        m.doc() = "pybind11 example";

        pybind11::class_<Hello>(m, "Hello")
            .def(pybind11::init())
            .def("say", &Hello::say);
    }
    // g++ -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` opencvcall.cpp -o py2cpp`python3-config --extension-suffix` -I /usr/local/anaconda3/bin

    //python 调用方式
    //1, 先通过构造器来构建实例，方法为 模块名.构造器名
    //2，调用对应的方法， 模块名.方法名
    //例如本例子需要如下调用
    // c=py2cpp.Hello()
    // c.say()
    
    //函数方法
    #include <pybind11/pybind11.h>

    int add( int i, int j ){
        return i+j;
    }

    PYBIND11_MODULE( py2cpp, m ){
        m.doc() = "pybind11 example";
        m.def("add", &add, "add two number" );
    }

    //在python中使用 模块名.函数名 来访问
    //例如本例子为  py2cpp.add(1,2)
### 11.1 cmake编译pybind11
    https://blog.csdn.net/luolinll1212/article/details/112907469  
    将编译好的文件要整个都放在与源文件相同的地方，注意：只有C++14才有处理pybind重载的功能。  
    也可以将编译好的文件安装, 再用find_package(pybind11 REQUIRED),再其的一样 
    
编译pybind11  

    git clone https://github.com/pybind/pybind11.git
    cd pybind11
    mkdir build
    cd build
    cmake ..
    cmake --build . --config Release --target check
    make check -j 4
    
CMakeLists.txt

    cmake_minimum_required(VERSION 2.8.12)
    project(example)
    add_subdirectory(pybind11) # 已经编译完的pybind11
    pybind11_add_module(example example.cpp)

### 11.2 cv2与cv::Mat进行通讯
在C++源文件中，添加转换函数  
mat_warper.h 

    #ifndef MAT_WARPER_H_

    #include <opencv2/opencv.hpp>
    #include <pybind11/pybind11.h>
    #include <pybind11/numpy.h>

    namespace py = pybind11;

    cv::Mat numpy_uint8_1c_to_cv_mat(py::array_t<unsigned char> &input);
    cv::Mat numpy_uint8_3c_to_cv_mat(py::array_t<unsigned char> &input);
    py::array_t<unsigned char> cv_mat_uint8_1c_to_numpy(cv::Mat &input);
    py::array_t<unsigned char> cv_mat_uint8_3c_to_numpy(cv::Mat &input);

    #endif // !MAT_WARPER_H_

mat_warper.cpp  

    #include "mat_warper.h"
    #include <pybind11/numpy.h>

    /*
    Python->C++ Mat
    */

    cv::Mat numpy_uint8_1c_to_cv_mat(py::array_t<unsigned char> &input)
    {
        if (input.ndim() != 2)
            throw std::runtime_error("1-channel image must be 2 dims ");
        py::buffer_info buf = input.request();
        cv::Mat mat(buf.shape[0], buf.shape[1], CV_8UC1, (unsigned char *)buf.ptr);
        return mat;
    }

    cv::Mat numpy_uint8_3c_to_cv_mat(py::array_t<unsigned char> &input)
    {
        if (input.ndim() != 3)
            throw std::runtime_error("3-channel image must be 3 dims ");
        py::buffer_info buf = input.request();
        cv::Mat mat(buf.shape[0], buf.shape[1], CV_8UC3, (unsigned char *)buf.ptr);
        return mat;
    }

    /*
    C++ Mat ->numpy
    */
    py::array_t<unsigned char> cv_mat_uint8_1c_to_numpy(cv::Mat &input)
    {
        py::array_t<unsigned char> dst = py::array_t<unsigned char>({input.rows, input.cols}, input.data);
        return dst;
    }

    py::array_t<unsigned char> cv_mat_uint8_3c_to_numpy(cv::Mat &input)
    {
        py::array_t<unsigned char> dst = py::array_t<unsigned char>({input.rows, input.cols, 3}, input.data);
        return dst;
    }

    //PYBIND11_MODULE(cv_mat_warper, m) {
    //
    //  m.doc() = "OpenCV Mat -> Numpy.ndarray warper";
    //
    //  m.def("numpy_uint8_1c_to_cv_mat", &numpy_uint8_1c_to_cv_mat);
    //  m.def("numpy_uint8_1c_to_cv_mat", &numpy_uint8_1c_to_cv_mat);
    //
    //
    //}


### 11.3 c++调用python
https://pybind11.readthedocs.io/en/stable/advanced/embedding.html  
cpp文件: 

    #include <pybind11/embed.h>
    #include <iostream>

    namespace py = pybind11;

    int main()
    {
        py::scoped_interpreter python;

        py::module sys = py::module::import("sys");
        py::print(sys.attr("path"));

        py::module t = py::module::import("tttt");
        t.attr("add")(1, 2);
        return 0;
    }
    
 cmakelists.txt
 
     cmake_minimum_required(VERSION 3.4...3.18)
    project(example LANGUAGES CXX)

    # add_subdirectory(pybind11)
    # pybind11_add_module(example test.cpp)


    find_package(pybind11)
    # pybind11_add_module(example test.cpp)

    add_executable(example test.cpp)
    target_link_libraries(example PRIVATE pybind11::embed)

tttt.py, 放在build文件中

    """tttt.py located in the working directory"""


    def add(i, j):
        print("hello,pybind11")
        return i + j



