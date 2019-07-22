# numpy
## 1. 扩充数据维度
### 方法1. np.expand_dims(a, axis=0)
表示在0轴添加数据,转换结果如下

    a = np.array([1, 2, 3])
    b = np.expand_dims(a, axis=0)
    b
    array([[1, 2, 3]])
### 方法2. np.newaxis
    x = np.random.randint(1, 8, size=5)
    #array([4, 6, 6, 6, 5])
    x1 = x[np.newaxis, :]
    x1
    #array([[4, 6, 6, 6, 5]])
    
## 2. 掩码赋值？
### code
    import numpy as np
    a = np.array([[1, 2, 3], [4, 5, 6]])
    a_backup = a.copy()
    print('赋值前：\n', a)
    b = np.array([[True, True, True], [False, False, False]])
    a[b] = 0
    print('赋值后：\n', a)
    c = a_backup[b]
    print('舍弃后：\n', c)
### out
    赋值前：
     [[1 2 3]
     [4 5 6]]
    赋值后：
     [[0 0 0]
     [4 5 6]]
    舍弃后：
     [1 2 3]

## 3. 相同顺序shuffle多个list
在使用np.random.shuffle之前,使用np.random.sees(int)来设置随机因子

    import numpy as np 

    a = np.arange(10)
    b = np.arange(10)
    print(a)
    print(b)
    np.random.seed(1)
    np.random.shuffle(a)
    np.random.seed(1)
    np.random.shuffle(b)
    print(a)
    print(b)
    
    out:
    [0 1 2 3 4 5 6 7 8 9]
    [0 1 2 3 4 5 6 7 8 9]
    [2 9 6 4 0 3 1 7 8 5]
### 注意
np.random.shuffle(x)会直接对x进行操作,函数返回值为None,x的内容会改变
    [2 9 6 4 0 3 1 7 8 5]

## 4. 标量shape
    a = np.array(3.14)
    print(a.shape)
    out:
    ()
    
    
# dlib
    #coding=utf-8

    import cv2
    import dlib

    path = "img/meinv.png"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #人脸分类器
    detector = dlib.get_frontal_face_detector()
    # 获取人脸检测器
    predictor = dlib.shape_predictor(
        "C:\\Python36\\Lib\\site-packages\\dlib-data\\shape_predictor_68_face_landmarks.dat"
    )
    # The 1 in the second argument indicates that we should upsample the image
    # 1 time.  This will make everything bigger and allow us to detect more
    # faces.
    dets = detector(gray, 1)
    for face in dets:
        shape = predictor(img, face)  # 寻找人脸的68个标定点
        # 遍历所有点，打印出其坐标，并圈出来
        for pt in shape.parts():
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)
        cv2.imshow("image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# logging
对打印的信息以级别来划分,根据在程序开头设置的级别,来打印适当级别的信息
## 1. 示例
    import logging
    # level=logging.WARNING和level=logging.INFO,输出打印信息数量不一样
    logging.basicConfig(filename = 'test.log', 
        level=logging.WARNING, 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')

## 2. 参数说明
### 2.1 format
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息
### 2.2 level
    DEBUG： 详细信息，通常仅在诊断问题时才受到关注。整数level=10
    INFO： 确认程序按预期工作。整数level=20
    WARNING：出现了异常，但是不影响正常工作.整数level=30
    ERROR：由于某些原因，程序 不能执行某些功能。整数level=40
    CRITICAL：严重的错误，导致程序不能运行。整数level=50
    
## 3. TimedRotatingFileHandler
    import logging
    from logging.handlers import TimedRotatingFileHandler

    log = logging.getLogger(loggerName)

    formatter = logging.Formatter('%(name)-12s %(asctime)s level-%(levelname)-8s thread-%(thread)-8d %(message)s')   # 每行日志的前缀设置
    fileTimeHandler = TimedRotatingFileHandler(BASIC_LOG_PATH + filename, "S", 1, 10)

    fileTimeHandler.suffix = "%Y%m%d.log"  #设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
    fileTimeHandler.setFormatter(formatter)
    logging.basicConfig(level = logging.INFO)
    fileTimeHandler.setFormatter(formatter)
    log.addHandler(fileTimeHandler)
    try:
        log.error(msg)
    except Exception, e:
        print "writeLog error"
    finally:
       log.removeHandler(fileTimeHandler)
       
### 3.1 分隔时间说明
    S 秒
    M 分钟
    H 小时
    D 天
    W 周
    midnight 在午夜

## 4. 与tensorflow关系
tf.logging的打印内容与logging的设置一致，可以logging.basicConfig(...),再让tensorflow打印出来


# functools
## reduce
    from functools import reduce

    def add(x, y):
        return x+y

    reduce(add, [1,2,3,4])
    
上面这段 reduce 代码，其实就相当于 1 + 2 + 3 + 4 = 10
