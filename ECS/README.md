## 1. 防火墙
    ## 1. 防火墙
    # 安装
    apt install firewalld
    # 开放端口
    firewall-cmd --zone=public --add-port=22/tcp --permanent
    firewall-cmd --zone=public --add-port=7000-8000/udp --permanent 
    # 使配置生效
    firewall-cmd --reload
    # 查看所有已经开放的端口
    firewall-cmd --zone=public --list-ports
    # 重新启动
    systemctl restart firewalld

    # 关闭端口
    firewall-cmd --zone=public --remove-port=22/tcp --permanent

## 2. ECS开发端口
1. 在阿里云中，找到实例->...->安全组规则  
2. 入方向->手动添加->目的（开放的端口号）->源（默认0.0.0.0）

## 3. NAT内网穿透
使用frp
下载frp

    $ wget https://github.com/fatedier/frp/releases/download/v0.21.0/frp_0.21.0_linux_amd64.tar.gz
    $ tar -xzvf frp_0.21.0_linux_amd64.tar.gz
    $ cd frp_0.27.0.0_linux_amd64
### 3.1 服务端
配置frps.ini

    [common]
    bind_port = 1234            #frp程序本身需要占用一个端口运行
    vhost_http_port = 555      #外网访问的端口，特定的http类型
运行

    ./frps -c ./frps.ini

### 3.2 本地客户端
配置frpc.ini   

    [common]
    server_addr = 100.10.11.12         #所购买的云主机公网IP地址
    server_port = 1234                 #frp程序本身占用的端口，要与云主机的bind_port一致


    [detect]                       #自定义命名
    type = http                    #flask使用的是http类型传输
    local_ip = 127.0.0.1           
    local_port = 666                  #本地flask部署的端口
    remote_port = 555                   #外网访问端口
    custom_domains = 100.10.11.12      #http类型端口传输需要指定一个域名，没有域名就写IP地址
运行

    ./frpc -c ./frpc.ini       #运行代码

### 3.3 后台运行
    // 运行
    $ nohup ./frps -c frps.ini &
    // 查看日志
    $ tail -f nohup.out

### 3.4 多客户端配置

    内网机器1：
    [ssh]                      <==不同点
    type = tcp 
    local_ip = 127.0.0.1
    local_port = 22
    remote_port = 6000         <==不同点
    
    内网机器2：
    [ssh1]                     <==不同点
    type = tcp 
    local_ip = 127.0.0.1
    local_port = 22
    remote_port = 6001         <==不同点


## 4. mysql连接 
### 4.1 连接远程mysql

    sudo apt-get install mysql-server mysql-client
    mysql -h 服务器ip地址 -P 3306 -u root -p





