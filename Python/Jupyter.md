## 1. 在服务器起服务
    $ nohup jupyter notebook --ip=0.0.0.0 &
    # 或者
    $ nohup jupyter notebook --ip 10.45.47.111 &
### 1.1 查看token
    $ jupyter notebook list
    Currently running servers:
    http://10.45.47.111:8889/?token=d43a2de4912f9764ea190eb5203ef40802116674d362c489 :: /mnt/hdd/home/liushu/liushu
### 1.2 访问
在浏览器中输入http://10.45.47.111:8889，输入token：  

    d43a2de4912f9764ea190eb5203ef40802116674d362c489

### 1.3 设置密码

    jupyter notebook password

注：生效需重启jupyter notebook, 或者在起服务器之前设置 

