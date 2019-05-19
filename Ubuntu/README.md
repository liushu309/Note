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
  <img src="../Image/folder_height_light.jpeg" alt="samples" width="400px">
</p>  
含义: 文件夹的权限全部开放，比如777, 可用chmod改变
