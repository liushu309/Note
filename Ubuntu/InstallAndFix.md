## 1. win10与Ubuntu双系统
  1> 用U大师制作U盘的启动盘（制作格式必须是Fast32），再在电脑上建立uefi分区，可以不用用软碟通把U盘制作成Win10启动盘  
  2> 按F2不动，进入bios设置启动顺序，按F5 F6上下调节顺序，设置U盘为第一启动，其它的不要设置，启动模式还是uefi模式  
  3> 在电脑上，把一个分区空出来  
  4> 用软碟通制作UbuntuU盘启动盘，写入方式一定要是RAW，不要选HDD之类  
  5> 将Secure Boot设为disable,以及Intel Platform Trust Technology设为disable
  6> 将上述的设为enable
  7> 如果有问题可以尝试以下步骤  
  
  1. GraphicDevice设为UMA Graphic（集成显卡模式），装成后再改回来  
  2. 安装后会跳出一个界面，选择lightdm  然后重启：reboot  
    
    sudo apt-get install lightdm



