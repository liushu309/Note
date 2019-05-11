## 连接github
    1> sudo apt-get install openssh-server openssh-client  
    2> sudo apt-get install git-core  
    3> ssh-keygen -C '670602937@qq.com' -t rsa  
    4> 默认生成的key在/home/.ssh/id_rsa.pub, 登录github-Account Settings-SSH Keys-Add SSH Key，title随意，粘贴SSH key  
    5> git config --global user.name "your name"  
       git config --global user.email "your email"  
    6> 测试：ssh -v git@github.com  
  
## 本地连接连接github
    1> github上创建一个仓库，地址 https://github.com/liushu309/test.git  
    2> 在本地上生成一个仓库，可以  
      git clone git@github.com:nanfei9330/xx.git  
    或者进入一个新的目录  
      git init  
    3> 关联  
      git remote add origin git@github.com/liushu309/test.git  
    4> 推送master分支的所有内容  
      git push -u origin master  
    第二次推送时，可以不用-u  
    5> 取回远程主机某个分支的更新  
      git pull origin master  
    再由本地更新github，可以使用  
      git push origin master  
    
## push时出现输入用户名密码
  因为与github连接的传输协议不一样，可能是https协议会出现这个问题
  ### 1. 查看连接方式
    git remote -v
    out:
    origin	https://github.com/liushu309/Note.git (fetch)
    origin	https://github.com/liushu309/Note.git (push)
  ### 2. 重新设置
    git remote rm origin
    git remote add origin git@github.com:username/repository.git
    git push -u origin master
