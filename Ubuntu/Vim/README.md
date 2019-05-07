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

## 4. 查找字符所在行
在命令模式下输入 / + '想查找的字符'

    :/ def train()
    
## 5. vim快捷键
    [shift + v]: 行选择
    [Ctrl + v]: 块选择
    y: 选择
    d: 删除
    p: 粘贴
    [Ctrl + s]: 锁
    [Ctrl + q]: 解锁
    [Ctrl + f]: 向下翻页
    [Ctrl + b]: 向后翻页
    1> 在一个窗口打开多个文件
    [:sp{filename}]: 再打开一个窗口，没有filename时，打开为同一个窗口
    [Ctrl + w + "上"\"下"]: 在两个窗口之间切换
