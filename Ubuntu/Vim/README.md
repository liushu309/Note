## 1. vim永久显示行号
    vim ~/.vimrc
    输入
    set number
## 2. 设置vim缩进大小为2
    vim ~/.vimrc
    输入
    set tabstop=2
    set expandtab    
    set smartindent
    set shiftwidth=2
## 3. 缩进
### 1> 在命令模式下输入
    // 从第2到第9行向右缩进一个tab
    2,9>
### 2> 行选择操作
    shift+v
    shift+>
