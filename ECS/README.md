## 1. 防火墙
    ## 1. 防火墙
    # 安装
    apt install firewall
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
