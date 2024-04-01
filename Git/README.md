## 1. 连接github
    1> sudo apt-get install openssh-server openssh-client  
    2> sudo apt-get install git-core  
    3> ssh-keygen -C '670602937@qq.com' -t rsa(win10也可以这样写)    
    4> 默认生成的key在/home/.ssh/id_rsa.pub, 登录github-Account Settings-SSH Keys-Add SSH Key，title随意，粘贴SSH key  
    5> git config --global user.name "your name"  
       git config --global user.email "your email"  
    6> 测试：ssh -v git@github.com  
  
## 2. 本地连接github
    1> github上创建一个仓库，地址 https://github.com/liushu309/test.git  
    2> 在本地上生成一个仓库，可以  
      git clone git@github.com:nanfei9330/xx.git  
    或者进入一个新的目录  
      git init  
    3> 关联  
      git remote add origin git@github.com:/liushu309/test.git       
      注意这里的写法，是在github.com后加“：”, 而不是加“/”
    4> 推送master分支的所有内容  
      git push -u origin master  
    第二次推送时，可以不用-u  
    5> 取回远程主机某个分支的更新  
      git pull origin master  
    再由本地更新github，可以使用  
      git push origin master  
    
## 3. push时出现输入用户名密码
  因为与github连接的传输协议不一样，可能是https协议会出现这个问题
  ### 1. 查看连接方式
    git remote -v
    out:
    origin	https://github.com/liushu309/Note.git (fetch)
    origin	https://github.com/liushu309/Note.git (push)
  ### 2. 重新设置ssh协议连接
    git remote rm origin
    git remote add origin git@github.com:username/repository.git
    git push -u origin master

## 4. 创建服务器
1. 创建仓库（这个服务器里只能保存文件，不能编辑，所以适合至少三个文件夹，一个服务器，两个编辑文件夹）

    $ git init --bare liushu.git  
    
如果想不想使用服务器，或者服务器里也可以有工作区，可以:

    $ git init liushu.git
    $ git config receive.denyCurrentBranch ignore
或者在.git/config文件中添加设置  

    [receive]
            denyCurrentBranch = ignore  
            
因此，当你设置 receive.denyCurrentBranch 为 ignore 时，你实际上是告诉 Git：允许直接推送更新到当前分支，即使这可能会覆盖其他人的工作。这通常用于你控制整个仓库的访问权限，并且确信这样做不会造成问题的情况。然而，在多人协作的项目中，通常建议避免这样做，因为它可能导致数据丢失或混淆。  
            
2. 注意：id_rsa.pub 文件不应该直接放在 ~/.ssh/authorized_keys 目录下或 ~/.ssh/ 目录下。实际上，id_rsa.pub 文件中的内容应该被添加到 ~/.ssh/authorized_keys 文件中。

3. 仓库名为包含.git文件夹的上级文件夹的名称，比如
   
    // git init，仓库的名称就是上级文件夹名称  
    git remote add origin liushu@192.168.2.7:/D:/Documents/FTP/server  
    // 如果是git init server，仓库名称就是server.git  
    git remote add origin liushu@192.168.2.7:/D:/Documents/FTP/server.git

4. 拉取的时候，不要直接使用git pull，而是git pull origin master  

## 4. 概念
### 1. git status -s 中的状态字母
新添加的未跟踪文件前面有 ?? 标记，  
新添加到暂存区中的文件前面有 A 标记，  
修改过的文件前面有 M 标记,  
M 有两个可以出现的位置，出现在右边的 M 表示该文件被修改了但是还没放入暂存区，出现在靠左边的 M 表示该文件被修改了并放入了暂存区。

### 2. 撤销操作
1. 还没 $ git add file 

        $ git reset HEAD <filename> 

2. 已经$ git add file, 但是没有 git commit -m "", 分两步操作

        $ git checkout -- <filename>
        $ git  status
        $ git checkout -- file
3. 从以前版本前进到后来版本

        $ git reflog  
        $ git reset --hard <edit_id>  
4. 注意两个地方  

        liushu@192.168.0.177:/home/...(1.本地的话用liushu; 2. com后接:再接/)

### 3. git push 和git pull
    $ git push <远程主机名> <本地分支名>  <远程分支名>
    $ git pull <远程主机名> <远程分支名>:<本地分支名>
    
    
## 5. pull子文件夹
示例:  
现在有一个test仓库https://github.com/mygithub/test  
需要gitclone里面的tt子目录：

    git init test && cd test     //新建仓库并进入文件夹
    git config core.sparsecheckout true //设置允许克隆子目录
    echo 'tt*' >> .git/info/sparse-checkout //设置要克隆的仓库的子目录路径   //空格别漏
    git remote add origin git@github.com:mygithub/test.git  //这里换成你要克隆的项目和库
    git pull origin master    //下载
### 注意
结果虽然只下载了选定的文件夹，但是可能.git文件还是全部下载下来了，所以存储空间和下载时间基本没有怎么变

## 6.git不起作用
    git rm -r --cached .
    git add .
    git commit -m 'update .gitignore'   //windows 使用的命令是  


## 7. gitlab搭建
    https://blog.csdn.net/EthanCo/article/details/82828097

## 8. authorized_keys使用注意事项
1. 该文件用户组权限为读和写，去掉用户组写权限即可。  
2. 生成密钥的登录用户要保持一致，各服务器的登录用户之间才能免密登录。
