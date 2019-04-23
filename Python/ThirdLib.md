# numpy
## 1. np.expand_dims(a, axis=0)
表示在0轴添加数据,转换结果如下

    a = np.array([1, 2, 3])
    b = np.expand_dims(a, axis=0)
    b
    array([[1, 2, 3]])
    
## 2. 掩码赋值？
    import numpy as np
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print('赋值前：\n', a)
    b = np.array([[True, True, True], [False, False, False]])
    a[b] = 0
    print('赋值后：\n', a)
    
    out:
    赋值前：
     [[1 2 3]
     [4 5 6]]
    赋值后：
     [[0 0 0]
     [4 5 6]]
