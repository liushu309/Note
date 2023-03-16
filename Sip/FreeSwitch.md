## 1. Ubuntu20.04安装freeswitch
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
