### 1. 添加清华镜像
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --set show_channel_urls yes
    
### 2. The repository located at mirrors.aliyun.com is not a trusted or secure host
安装时加入

    –-trusted-host mirrors.aliyun.com
比如

    pip install beautifulsoup4 --trusted-host mirrors.aliyun.com
