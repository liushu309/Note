## 1. cpp文件
    #include <opencv2/opencv.hpp>

    using namespace cv;

    extern "C"
    {
        uchar *cpp_canny(int height, int width, uchar *data)
        {
            cv::Mat src(height, width, CV_8UC1, data);
            cv::Mat dst;
            Canny(src, dst, 100, 200);

            uchar *buffer = (uchar *)malloc(sizeof(uchar) * height * width);
            memcpy(buffer, dst.data, height * width);
            return buffer;
        }

        void release(uchar *data)
        {
            free(data);
        }
    }
    
### 1.1 CMakeLists.txt文件
    cmake_minimum_required(VERSION 3.9)

    project(demo)

    find_package(OpenCV REQUIRED)

    add_library(opencvcall SHARED opencvcall.cpp)

    target_link_libraries(opencvcall ${OpenCV_LIBS})


## 2. python文件
    import cv2
    from numpy.ctypeslib import ndpointer
    import ctypes
    import numpy as np

    # dll=ctypes.WinDLL('MyDLL.dll')
    ll = ctypes.cdll.LoadLibrary
    lib = ll("./build/libopencvcall.so")


    def cpp_canny(input):
        if len(img.shape) >= 3 and img.shape[-1] > 1:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        h, w = gray.shape[0], gray.shape[1]

        # 获取numpy对象的数据指针
        frame_data = np.asarray(gray, dtype=np.uint8)
        frame_data = frame_data.ctypes.data_as(ctypes.c_char_p)

        # 设置输出数据类型为uint8的指针
        lib.cpp_canny.restype = ctypes.POINTER(ctypes.c_uint8)

        # 调用dll里的cpp_canny函数
        pointer = lib.cpp_canny(h, w, frame_data)

        # 从指针指向的地址中读取数据，并转为numpy array
        np_canny = np.array(np.fromiter(pointer, dtype=np.uint8, count=h*w))

        return pointer, np_canny.reshape((h, w))


    img = cv2.imread(
        '/home/liushu/Documents/DataSet/WQ_dataset/Image/554/554_00001.jpg')
    ptr, canny = cpp_canny(img)
    cv2.imshow('canny', canny)
    cv2.waitKey(2000)
    # 将内存释放
    lib.release(ptr)
