## 0. vi三种模式
    1. 一般模式: 刚进入vi时的模式，可以进行复制粘贴
    2. 编辑模式: 比如按了键i
    3. 命令行模式: 比如按了:

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
1. 在命令模式下输入 / + '想查找的字符'  
2. 查找下一个按'n', 查找上一个按'N'

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
    [dd]: 删除整行
    [shift + 4]: 移动到行尾($)
    [shift + Ctrl + F]: 在終端搜索字符
    [shift + -]： 移动到行首(_)
    u: 命令模式下撤消一步操作
    [Ctrl + r]: 命令模式下前进一步操作

## 6. vi多行注释
1. ctrl+v选中行  
2. 输入I（大写的i），在道行输入信息    
3. 写上#，再按Esc自动退出  


## 7. 查找字符串
    # 替换当前行，其中g是替换标志，代表global的意思，也可以换成c：需要确认；i:大小写不敏感；I：大小写敏感
    ：s/old/new/g 
    # 全局替换
    ：%s/old/new/g
    # 替换特定行
    ：m,ns/old/new/g
    # 选择区域替换
    ：'<,'>s/old/new/g                #先visual模式下选择要替换的区域 
    
## 8. 分窗打开文件 
同时打开多个窗口  

    vim -o liushu_1.txt liushu_2.txt

在使用过程中打开多个窗口  

    :split liushu_2.txt
    # 或者
    :sp liushu_2.txt

窗口之间的切换  

    # 循环切换
    ctrl + w + w
