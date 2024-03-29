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

### 11.4将纯python脚本转成os文件
sudo apt  install python-dev gcc   
pip install cython
再写脚本set_up.py

    from distutils.core import setup
    from Cython.Build import cythonize

    setup(
        ext_modules=cythonize("add_num.py[即要编译的python文件]")
    )

python set_up.py build_ext --inplace  
--inplace是在当前文件生成库


## 12. python装饰器
import time

def Time_statistics(装饰器参数):
    def inner(修饰的函数名):
        def wraper(*修饰函数参数列表, **修饰函数参数字典):

            # 最后返回的替换代码可能只有下面这些，return ret可能只是为了给装饰器一个类型检查
            time_start = time.time()                                          # <-----
            for i in range(装饰器参数):                                        # <-----
                ret = 修饰的函数名(*修饰函数参数列表, **修饰函数参数字典)         # <-----
            time_end = time.time()                                            # <-----
            print(f'{time_end - time_start} time spaced')                     # <-----
            return ret                                                        # return 好像可以不要，但是不要的话会报错
        return wraper     
    return inner

@Time_statistics(10)
def print_info(info):
    print(f'{info} ----<')

if __name__ == "__main__":
    print_info('hello world')


### 13. python发送邮件
http://t.zoukankan.com/jiliangceshi-p-13220082.html  
1. 去163获取邮箱发送邮件的授权码    
2. python代码  

        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        # 发送邮件相关参数
        smtpserver = 'smtp.163.com'         # 发件服务器
        port = 0                            # 端口
        sender = 'wqkj7001@163.com'         # 发件人邮箱
        psw = 'xxxxxxxxxxxxxxxx'            # 发件人授权码
        receiver = ["670602937@qq.com","wqkj7002@163.com"]      # 接收人
        # 邮件标题
        subjext = 'python发送附件邮件'
        # 获取附件信息
        with open('vue_script.html', "r", encoding='utf-8') as f:
            body = f.read()
        message = MIMEMultipart()
        # 发送地址
        message['from'] = sender
        # message['to'] = receiver
        message['to'] = "无邪"
        message['subject'] = subjext
        # 正文
        body = MIMEText(body, 'plain', 'utf-8')
        message.attach(body)
        # 同一目录下的文件
        att = MIMEText(open('./sample.py', 'rb').read(), 'base64', 'utf-8') 
        att["Content-Type"] = 'application/octet-stream'
        # filename附件名称
        att["Content-Disposition"] = 'attachment; filename="sample.py"'
        message.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)    # 链接服务器
        smtp.login(sender, psw)     # 登录
        smtp.sendmail(sender, receiver, message.as_string())  # 发送
        smtp.quit()             # 关闭


### 14. python线程之间的通信
threading.Thread(target=, args=, ...)  
单个变量可以使用锁Lock()，多个变量如数据传输，可以使用单向队列queue.Queue()  

    import queue
    from time import sleep
    from random import choice
    from threading import Thread, Lock

    book_num = 100  # 图书馆最开始有100本图书
    bookLock = Lock()

    def books_return():
        global book_num
        while True:
            bookLock.acquire()
            book_num += 1
            print("归还1本，现有图书{}本".format(book_num))
            bookLock.release()
            sleep(1)  # 模拟事件发生周期


    def books_lease():
        global book_num
        while True:
            bookLock.acquire()
            book_num -= 1
            print("借走1本，现有图书{}本".format(book_num))
            bookLock.release()
            sleep(2)  # 模拟事件发生周期


    # maxsize小于等于0的时候队列无限大
    q = queue.Queue(maxsize=5)
    dealList = ["红烧猪蹄", "卤鸡爪", "酸菜鱼", "糖醋里脊", "九转大肠", "阳春面", "烤鸭", "烧鸡", "剁椒鱼头", "酸汤肥牛", "炖羊肉"]

    def cooking(chefname: str):
        for i in range(4):
            deal = choice(dealList)
            q.put(deal, block=True)
            print("厨师{}给大家带来一道：{}  ".format(chefname, deal))


    def eating(custname: str):
        for i in range(3):
            deal = q.get(block=True)
            print("顾客{}吃掉了：{}  ".format(custname, deal))
            q.task_done()


    if __name__ == "__main__":
        # 使用锁
        thread_lease = Thread(target=books_lease)
        thread_return = Thread(target=books_return)
        thread_lease.start()
        thread_return.start()

        # 使用队列
        # 创建并启动厨师ABC线程，创建并启动顾客1234线程
        threadlist_chef = [Thread(target=cooking, args=chefname).start() for chefname in ["A", "B", "C"]]
        threadlist_cust = [Thread(target=eating, args=str(custname)).start() for custname in range(4)]
        # 队列阻塞，直到所有线程对每个元素都调用了task_done
        q.join()






