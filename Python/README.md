## python加入包路径
### 1. 在包路径下创建文件
    __init__.py
### 2. 在里面复制以下代码
    import os
    import sys

    rootpath = str(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(rootpath)
    
### 3. python “...”操作符
在Python中，“...”(ellipsis)操作符，表示其他维度不变，只操作最前或最后1维

    import numpy as np
    
    x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    """[[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12]]"""
    print(x.shape)  # (3, 4)
    y = x[1:2, ...]
    """[[5 6 7 8]]"""
    print(y)

### 4. python "::-1"
“::-1”是颠倒数组的值，例如：  

    import numpy as np

    a = np.array([1, 2, 3, 4, 5])
    print a[::-1]
    """[5 4 3 2 1]"""
