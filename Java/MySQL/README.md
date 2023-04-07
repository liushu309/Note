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

## 3. 关系数据库概念
1. 外键：外键是指引用另一个表中的一列或多列，被引用的列应该具有主键约束或唯一性约束。在另一个表中当主键的字段。
##＃ 3.1 连接方式
join方式：  
1. 交叉连接（cross join, 笛卡尔积）  
2. 内连接（inner join）  
3. 外连接（outerjoin, 包括左连接, 右连接） 

epm_info  

    +------+-------+------+------------+--------+   
    | id   | name  | age  | address    | salary |  
    +------+-------+------+------------+--------+  
    |    1 | Paul  |   32 | California |  20000 |  
    |    2 | Allen |   25 | Texas      |  15000 |  
    |    3 | Teddy |   23 | Norway     |  20000 |  
    |    4 | Mark  |   25 | Rich-Mond  |  65000 |  
    |    5 | David |   27 | Texas      |  85000 |  
    |    6 | Kim   |   22 | South-Hall |  45000 |  
    |    7 | James |   24 | Houston    |  10000 |  
    +------+-------+------+------------+--------+  

depm_info  

    +------+-------------+--------+  
    | id   | dept        | emp_id |  
    +------+-------------+--------+  
    |    1 | IT Billing  |      1 |  
    |    2 | Engineering |      2 |  
    |    3 | Finance     |      7 |  
    |    4 | 税务        |      2 |  
    +------+-------------+--------+  

### 1.1 cross join
生成两张表的笛卡尔积，返回的记录数为两张表记录数的乘积。  

    mysql> select * from emp_info, dept_info;
    +------+-------+------+------------+--------+------+-------------+--------+
    | id   | name  | age  | address    | salary | id   | dept        | emp_id |
    +------+-------+------+------------+--------+------+-------------+--------+
    |    1 | Paul  |   32 | California |  20000 |    4 | 税务        |      2 |
    |    1 | Paul  |   32 | California |  20000 |    3 | Finance     |      7 |
    |    1 | Paul  |   32 | California |  20000 |    2 | Engineering |      2 |
    |    1 | Paul  |   32 | California |  20000 |    1 | IT Billing  |      1 |
    |    2 | Allen |   25 | Texas      |  15000 |    4 | 税务        |      2 |
    |    2 | Allen |   25 | Texas      |  15000 |    3 | Finance     |      7 |
    |    2 | Allen |   25 | Texas      |  15000 |    2 | Engineering |      2 |
    |    2 | Allen |   25 | Texas      |  15000 |    1 | IT Billing  |      1 |
    |    3 | Teddy |   23 | Norway     |  20000 |    4 | 税务        |      2 |
    |    3 | Teddy |   23 | Norway     |  20000 |    3 | Finance     |      7 |
    |    3 | Teddy |   23 | Norway     |  20000 |    2 | Engineering |      2 |
    |    3 | Teddy |   23 | Norway     |  20000 |    1 | IT Billing  |      1 |
    |    4 | Mark  |   25 | Rich-Mond  |  65000 |    4 | 税务        |      2 |
    |    4 | Mark  |   25 | Rich-Mond  |  65000 |    3 | Finance     |      7 |
    |    4 | Mark  |   25 | Rich-Mond  |  65000 |    2 | Engineering |      2 |
    |    4 | Mark  |   25 | Rich-Mond  |  65000 |    1 | IT Billing  |      1 |
    |    5 | David |   27 | Texas      |  85000 |    4 | 税务        |      2 |
    |    5 | David |   27 | Texas      |  85000 |    3 | Finance     |      7 |
    |    5 | David |   27 | Texas      |  85000 |    2 | Engineering |      2 |
    |    5 | David |   27 | Texas      |  85000 |    1 | IT Billing  |      1 |
    |    6 | Kim   |   22 | South-Hall |  45000 |    4 | 税务        |      2 |
    |    6 | Kim   |   22 | South-Hall |  45000 |    3 | Finance     |      7 |
    |    6 | Kim   |   22 | South-Hall |  45000 |    2 | Engineering |      2 |
    |    6 | Kim   |   22 | South-Hall |  45000 |    1 | IT Billing  |      1 |
    |    7 | James |   24 | Houston    |  10000 |    4 | 税务        |      2 |
    |    7 | James |   24 | Houston    |  10000 |    3 | Finance     |      7 |
    |    7 | James |   24 | Houston    |  10000 |    2 | Engineering |      2 |
    |    7 | James |   24 | Houston    |  10000 |    1 | IT Billing  |      1 |
    +------+-------+------+------------+--------+------+-------------+--------+

### 1.2 inner join
生成两张表的交集，返回的记录数为两张表的交集的记录数。 

    mysql> select * from emp_info inner join dept_info on emp_info.id=dept_info.emp_id;
    +------+-------+------+------------+--------+------+-------------+--------+
    | id   | name  | age  | address    | salary | id   | dept        | emp_id |
    +------+-------+------+------------+--------+------+-------------+--------+
    |    1 | Paul  |   32 | California |  20000 |    1 | IT Billing  |      1 |
    |    2 | Allen |   25 | Texas      |  15000 |    4 | 税务        |      2 |
    |    2 | Allen |   25 | Texas      |  15000 |    2 | Engineering |      2 |
    |    7 | James |   24 | Houston    |  10000 |    3 | Finance     |      7 |
    +------+-------+------+------------+--------+------+-------------+--------+
    
### 1.3 outer join
1. left join  
left join(A, B), 返回表A的所有记录，另外表B中匹配的记录有值，没有匹配的记录返回null。 
 
    mysql> select * from emp_info left join dept_info on emp_info.id=dept_info.emp_id;  
    +------+-------+------+------------+--------+------+-------------+--------+
    | id   | name  | age  | address    | salary | id   | dept        | emp_id |
    +------+-------+------+------------+--------+------+-------------+--------+
    |    1 | Paul  |   32 | California |  20000 |    1 | IT Billing  |      1 |
    |    2 | Allen |   25 | Texas      |  15000 |    4 | 税务        |      2 |
    |    2 | Allen |   25 | Texas      |  15000 |    2 | Engineering |      2 |
    |    3 | Teddy |   23 | Norway     |  20000 | NULL | NULL        |   NULL |
    |    4 | Mark  |   25 | Rich-Mond  |  65000 | NULL | NULL        |   NULL |
    |    5 | David |   27 | Texas      |  85000 | NULL | NULL        |   NULL |
    |    6 | Kim   |   22 | South-Hall |  45000 | NULL | NULL        |   NULL |
    |    7 | James |   24 | Houston    |  10000 |    3 | Finance     |      7 |
    +------+-------+------+------------+--------+------+-------------+--------+


2. right join(A, B), 返回表B的所有记录，另外表A中匹配的记录有值，没有匹配的记录返回null。 
 
    mysql> select * from emp_info right join dept_info on emp_info.id=dept_info.emp_id;

    +------+-------+------+------------+--------+------+-------------+--------+
    | id   | name  | age  | address    | salary | id   | dept        | emp_id |
    +------+-------+------+------------+--------+------+-------------+--------+
    |    1 | Paul  |   32 | California |  20000 |    1 | IT Billing  |      1 |
    |    2 | Allen |   25 | Texas      |  15000 |    2 | Engineering |      2 |
    |    7 | James |   24 | Houston    |  10000 |    3 | Finance     |      7 |
    |    2 | Allen |   25 | Texas      |  15000 |    4 | 税务        |      2 |
    +------+-------+------+------------+--------+------+-------------+--------+
    


