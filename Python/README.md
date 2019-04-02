## python加入包路径
### 1. 在包路径下创建文件
    __init__.py
### 2. 在里面复制以下代码
    import os
    import sys

    rootpath = str(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(rootpath)
