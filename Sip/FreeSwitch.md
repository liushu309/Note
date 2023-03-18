## 1. 学习建议
如果想要快速学习Freeswitch，可以按照以下步骤：  
从基础开始：了解Freeswitch的架构、组件和安装。  
探索配置：熟悉基于XML的配置文件以及如何修改它们以适应您的需求。  
使用拨号计划：了解拨号计划语法、如何路由呼叫以及如何使用变量。  
学习模块：Freeswitch具有广泛的模块集合，可用于为您的PBX添加功能。了解最常用的模块。  
尝试高级功能：一旦您对基础知识有了很好的了解，可以尝试尝试更高级的功能，例如呼叫录音、会议和IVR。  
加入社区：Freeswitch社区活跃且乐于助人。加入论坛、邮件列表和IRC频道以获取帮助、分享经验并向他人学习。  
您可以参考以上步骤，快速掌握Freeswitch并开始构建自己的PBX。[1][2][3]  

References:  
[1] FreeSwitch Training - VoIP School  
[2] Installing and Setting up FreeSWITCH: Basics - Udemy  
[3] Introduction | FreeSWITCH Documentation - SignalWire API   

## 2. Ubuntu20.04安装freeswitch
参考：https://blog.csdn.net/weixin_39257042/article/details/109689112

    sudo apt install -y git subversion build-essential autoconf automake libtool libncurses5 libncurses5-dev make libjpeg-dev libtool libtool-bin libsqlite3-dev libpcre3-dev libspeexdsp-dev libldns-dev libedit-dev yasm liblua5.2-dev libopus-dev cmake

    sudo apt install -y libcurl4-openssl-dev libexpat1-dev libgnutls28-dev libtiff5-dev libx11-dev unixodbc-dev libssl-dev python-dev zlib1g-dev libasound2-dev libogg-dev libvorbis-dev libperl-dev libgdbm-dev libdb-dev uuid-dev libsndfile1-dev

    // 需要这样安装cmake，才能使用sudo cmake
    sudo apt install -y cmake

    // 需要另外添加的库
    sudo apt install libpq-dev libswscale-dev libavformat-dev

    cd ~/Desktop
    sudo git clone https://github.com/signalwire/libks.git
    cd libks
    sudo cmake .
    sudo make
    sudo make install
    ​
    cd ~/Desktop
    git clone https://github.com/signalwire/signalwire-c.git
    cd signalwire-c
    sudo cmake .
    sudo make
    sudo make install
    cd ~/Desktop
    sudo wget https://files.freeswitch.org/freeswitch-releases/freeswitch-1.10.3.-release.zip
    sudo apt -y install unzip
    sudo unzip freeswitch-1.10.3.-release.zip
    cd freeswitch-1.10.3.-release/
    ​
    ​
    sudo apt -y install unzip
    ​
    // 安装新的库后，sudo cmake前必需重新运行sudo ./configure -C
    sudo ./configure -C
    sudo make
    ​
    sudo ./configure && sudo make clean && sudo make
    sudo make install

    sudo make all cd-sounds-install cd-moh-install
    sudo ln -s /usr/local/freeswitch/bin/freeswitch /usr/bin/
    sudo ln -s /usr/local/freeswitch/bin/fs_cli /usr/bin
