## 1. Unable to access “文档”
    sudo ntfsfix /dev/sda5

## 2. 五笔输入法安装
  1> sudo apt-get install fcitx-table-wubi，重启  
  2> 在System Setting->Language Support中，最下面Keyboard input method system，由ibus切换成fcitx  
  3> 在桌面最右上角，点击输入法->Text Entry Setting...->添加wubi 和 pinyin  
  4> 繁体简体切换：shift + ctrl + f

## 3. 不自动隐藏菜单栏
  SystemSetting->Appearance->Behavior, 选In the menu bar和Always displayed

## 4. 修复安装
    sudo apt -f install

## 5. win与Ubuntu系统时间不一致
    sudo  timedatectl set-local-rtc true

## 6. 温度监控
    sudo apt-get install lm-sensors hddtemp
    sudo sensors-detect
    sensors
    sudo apt-get install psensor
  在Psensor中设置开机启动
  在Sensor Preferences中设置显示项 Application indicator Display sensor in the label

## 7. 实时查看gpu占用率
  watch -n 10 nvidia-smi
  
## 8. commond >out.txt 2>&1
0:标准输入, 1: 标准输出, 2:标准错误输出
将标准错误输出 重定向到 标准输出中,&的作用是使1不是文件名,而是标准输出1

## 9. 暂停在终端命令行运行的程序
    $ Ctrl + Z 暂停运行
    $ fg # 拉到前台继续运行
    $ bg # 挂到后台运行
    
## 10. 软硬鏈接
### 1. 软链接
    $ ln -s aaa bbbb
可以理解为把aaa文件夹创建了一个名字为bbb的快捷方式
### 2. 硬链接
    $ ln aaa bbb
可以理解为硬盘上有两个相同的文件夹或文件，他们之间的内容是实时同步的，實際只是添加將aaa作爲了一個node，指向和bbb一樣的物理地址？

## 11. 全绿色背景文件
全绿色高亮背景，如图  
<p align="center">
  <img src="../Image/folder_height_light.png" alt="samples" width="600px">
</p>  
含义: 文件夹的权限全部开放，比如777, 可用chmod改变

## 12. 查看当前文件夹占用空间
du : Disk usage  
-s或--summarize  仅显示总计，只列出最后加总的值。  
-h或--human-readable  以K，M，G为单位，提高信息的可读性。  

    $ du -hs
    35G     .

## 13. 关闭标签
ctrl + d

## 14. 修改密码
passwd xxx

## 15. pip换源
修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：

    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple

### pip国内的一些镜像

    阿里云 http://mirrors.aliyun.com/pypi/simple/ 
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
    豆瓣(douban) http://pypi.douban.com/simple/ 
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
    中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/    

## 16. 查看文件数量
1. 查看当前目录下的文件数量（不包含子目录中的文件）

    ls -l|grep "^-"| wc -l
2. 简写输出第一个

    l|wc


## 17. 删除指定类型文件
    find . -name '*.exe' -type f -print -exec rm -rf {} \;
(1) "."    表示从当前目录开始递归查找  
(2) “ -name '*.exe' "根据名称来查找，要查找所有以.exe结尾的文件夹或者文件  
(3) " -type f "查找的类型为文件  
(4) "-print" 输出查找的文件目录名  
(5) 最主要的是是-exec了，-exec选项后边跟着一个所要执行的命令，表示将find出来的文件或目录执行该命令。  
     exec选项后面跟随着所要执行的命令或脚本，然后是一对儿{}，一个空格和一个\，最后是一个分号  
