## 1. win10与Ubuntu双系统
  1> 用U大师制作U盘的启动盘（制作格式必须是Fast32），再在电脑上建立uefi分区，可以不用用软碟通把U盘制作成Win10启动盘  
  2> 按F2不动，进入bios设置启动顺序，按F5 F6上下调节顺序，设置U盘为第一启动，其它的不要设置，启动模式还是uefi模式  
  3> 在电脑上，把一个分区空出来  
  4> 用软碟通制作UbuntuU盘启动盘，写入方式选USB-HDD+,便捷启动里选“Syslinux”  
  ~~5> 将Secure Boot设为disable ~~  
  ~~6> 将上述的设为enable~~    
  ~~7> 如果有问题可以尝试以下步骤~~  
  
  ~~1. GraphicDevice设为UMA Graphic（集成显卡模式），装成后再改回来~~  
  ~~2. 安装后会跳出一个界面，选择lightdm  然后重启：reboot~~  
    
    ~~sudo apt-get install lightdm~~
 ~~要重新切换，写如下段落~~  
 
     ~~sudo dpkg-reconfigure lightdm~~
    
  8> 禁用显卡，后再立马装驱动
  
  $sudo vi /etc/modprobe.d/blacklist-nouveau.conf
  
      blacklist nouveau
      options nouveau modeset=0
  $sudo update-initramfs -u


9> sudo /etc/default/grub  

splash后加nomodeset

10> lightdm循环登录  
报错显示accounts-daemon.service is masked。是AccountsService的一部分。这个服务被禁用导致系统无法获取用户密码并打开session。运行下列命令解除禁用：

    sudo systemctl unmask accounts-daemon.service
之后再次reboot，gdm3成功进入桌面。完美解决问题。


11> 显卡安装  
1. 在安装显卡之前，先使用集显将亮度调低，再安装nvidia-smi
2. 使用高版本的离线文件安装nvidia-driver，比如cuda11.0, 不要使用sudo apt install nvidia-driver-460之类
3. 亮度调节

        sudo add-apt-repository ppa:apandada1/brightness-controller
        sudo apt update
        sudo apt install brightness-controller
        brightness-controller

12> grub文件配置

    #GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
    #GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_osi=Linux"
    #GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_backlight=vendor"
    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash text"
    #属性名：内核启动参数的默认值
    #值说明：quiet splash为不显示启动信息，安静的启动，如值为空则显示启动信息

    #GRUB_CMDLINE_LINUX="acpi_backlight=vendor"
    #GRUB_CMDLINE_LINUX="acpi_osi=Linux acpi_backlight=vendor"
    GRUB_CMDLINE_LINUX=""
