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
    
    // 一般脚本后台远行代码
    nohup /root/runoob.sh > runoob.log 2>&1 &

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

### 4.2 安装后登录密码及设置

没有设置root密码的情形  
    
    /etc/mysql/debian.cnf文件中，找到对应的debian-sys-maint用户名，注意这里不是root!，再输入对应的密码：  
    在终端上输入mysql -u debian-sys-maint -p，遇见输入密码的提示直接回车即可,进入MySQL后，分别执行下面三句话：  
    use mysql;  然后敲回车  
    update user set authentication_string=password("你的密码") where user="root";  然后敲回车  
    ***注意，这里最好也把debian-sys-maint的密码也改了，因为如果服务器的密码被知道了，所有的信息别人也看得见。
    flush privileges;  然后敲回车  
    重启  
    
debian-sys-maint给root赋权  

    使用debian-sys-maint账号给root账号提权，不然使用root账号无法创建、删除database;
    GRANT ALL PRIVILEGES ON *.* TO root@'localhost' IDENTIFIED BY '123456'  with grant option;
    查看权限，一般出现两行可能是权限最大的，如果有很长的一串显示转行，那么可能权限不够
    show grants for 'root'@'localhost';
    mysql> show grants for 'root'@'localhost';
    +---------------------------------------------------------------------+
    | Grants for root@localhost                                           |
    +---------------------------------------------------------------------+
    | GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
    | GRANT PROXY ON ''@'' TO 'root'@'localhost' WITH GRANT OPTION        |
    +---------------------------------------------------------------------+

远程：   

    1. 改表法（最好不要使用，因为加降低安全性，被要BTC）  
    
    use mysql;
    update user set host = '%' where user = 'root';
    flush privileges;
    quit;
    重启
    systemctl mysql restart
    
    2. 修改/etc/mysql/mysql.conf.d/mysqld.cnf配置文件。  
    
    打开配置文件，找到bind-address = 127.0.0.1这一行  
    改为bind-address = 0.0.0.0即可或简单一点注释掉也行  
    修改完成保存后，需要重启MySQL服务才会生效  


### 4.3 mysql 怎么导入/执行.SQL（存储过程）文件
方法一 进入命令行  
mysql –u用户名 –p密码 –D数据库【sql脚本文件路径全名】，示例：

    mysql –uroot –p123456 -Dtest</home/zj/create_table.sql

方法二 进入mysql的控制台后，使用source命令执行  
Mysqlsource 【sql脚本文件的路径全名】 或 Mysql\. 【sql脚本文件的路径全名】，示例：

    source /home/zj/create_table.sql

导入失败，如： (HY000): Unknown collation: 'utf8mb4_0900_ai_ci'，尝试以下步骤：  
1. 把文件中的所有的utf8mb4_0900_ai_ci替换为utf8_general_ci;  
2. 以及utf8mb4替换为utf8。  
