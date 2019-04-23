# numpy
## 1. np.expand_dims(a, axis=0)
表示在0轴添加数据,转换结果如下

    a = np.array([1, 2, 3])
    b = np.expand_dims(a, axis=0)
    b
    array([[1, 2, 3]])
