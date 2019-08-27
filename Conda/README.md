### 1. 添加清华镜像
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --set show_channel_urls yes
    
### 2. The repository located at mirrors.aliyun.com is not a trusted or secure host
安装时加入

    –-trusted-host mirrors.aliyun.com
比如

    pip install beautifulsoup4 --trusted-host mirrors.aliyun.com

### 3. opencv无法显示问题
1.卸载现在的版本  

     conda uninstall ...
2.使用下面命令重新安装  

    conda install -c menpo opencv3


### 4. pip --user
  没有权限时这样安装，可以只在自己时使用，注意--user不需要更改成--liushu，就是--user


### 5. 安裝PIL
    conda install pillow
