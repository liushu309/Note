# numpy
## 1. np.expand_dims(a, axis=0)
表示在0轴添加数据,转换结果如下

    a = np.array([1, 2, 3])
    b = np.expand_dims(a, axis=0)
    b
    array([[1, 2, 3]])
    
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
