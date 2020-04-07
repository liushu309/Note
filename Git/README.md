## 1. 连接github
    1> sudo apt-get install openssh-server openssh-client  
    2> sudo apt-get install git-core  
    3> ssh-keygen -C '670602937@qq.com' -t rsa  
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
      git remote add origin git@github.com/liushu309/test.git       
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
1. 创建仓库

    $ git init --bare liushu.git  
    
如果想不想使用服务器，或者服务器里也可以有工作区，可以:

    $ git init liushu.git
    $ git config receive.denyCurrentBranch ignore
或者在.git/config文件中添加设置  

    [receive]
            denyCurrentBranch = ignore
            
2. 在 ~/.ssh/authorized_keys加入访问电脑的id_rsa.pub,或者把id_rsa.pub（推荐重命名一下）放在服务器的~/.ssh目录下。

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


