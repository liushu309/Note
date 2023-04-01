## 1. 常见错误
### 1.1 ERROR 2003 (HY000): Can't connect to MySQL server on 'localhost:3306' (10061)
mysql服务没有启动，无法登录，去服务那里启动就可以了。（右键计算机->管理->服务->MySQL80->启动[自动]）

## 2. 忘记root密码
1. 路过权限验证

    sudo vim /etc/my.cnf

    [mysqld]
    skip-grant-tables

2. 免密登录，刷新权限表

    重启
    sudo systemctl stop mysql
    sudo systemctl start mysql
    mysql -u root
    flush privileges;

3. root的旧密码置空

    use mysql;
    update user set authentication_string='' where user='root';
    备注：Mysql5.7+ password字段 已改成 authentication_string字段

4. 重置密码

    alter user 'root'@'localhost' identified by 'newpassword';
    备注：Mysql8.0修改密码方式已有变化（此处是个坑，需要注意）
    Mysql8.0之前：
    update user set password=password('root') where user='root';

5. 注释免密登录

    sudo vim /etc/my.cnf
    #[mysqld]
    #skip-grant-tables

6. 重启登录

    sudo systemctl stop mysql
    sudo systemctl start mysql
    
    mysql -uroot -p
