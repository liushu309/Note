## 1. 安装教程
https://blog.csdn.net/EthanCo/article/details/82828097
### 1.1 主要步骤
    1. 安装信赖
    sudo apt-get update
    sudo apt-get install -y curl openssh-server ca-certificates
    sudo apt-get install -y postfix
    使用左右键和回车键选择确定、取消，弹出列表选项的时候，选择 Internet Site
    2. 接着信任 GitLab 的 GPG 公钥
    curl https://packages.gitlab.com/gpg.key 2> /dev/null | sudo apt-key add - &>/dev/null  
    3. 写入源
    sudo vi /etc/apt/sources.list.d/gitlab-ce.list  
    
    deb https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu xenial main
    4. 安装gitlab-ce
    sudo apt-get update
    sudo apt-get install gitlab-ce
    5. 执行配置与启动
    sudo gitlab-ctl reconfigure
    sudo gitlab-ctl start
### 1.2 设置root密码
第一次进入，需要输入管理员账号root的密码，以方便后期的管理。
### 1.3 配置域名

    sudo gedit /etc/gitlab/gitlab.rb 
    ＃external_url 'http://gitlab.example.com'  
    external_url 'http://192.168.39.100:7800'  
    sudo gitlab-ctl reconfigure  
