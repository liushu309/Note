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

4. 拉取的时候，不要直接使用git pull，而是git pull origin master, 而推送则是git push -u origin master    
5. 在win10上这些可能不成功，在ubuntu上没有问题。
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
    第一次pull之后一般要和本地的分支合并之后，才能push
    合并两个没有共同祖先的分支：在保留分支（master)中运行：git merge remotes/origin/master --allow-unrelated-histories 
    diff 旧的序列号 新的序列号
    
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

## 9. 工程配置
1. Qt和C++工程

    # Qt 工程相关  
    *.o  
    *.moc  
    Makefile  
    *.pro.user  
    *.files  
    build/  
    release/  
    debug/  
    .qmake.stash  
    .qmake.cache  
      
    # Python 工程相关  
    **/*.pyc  
    **/*.pyo  
    **/test/temp/  
    **/*.test.log  
    **/venv/  
    **/env/  
    .idea/  
    .DS_Store  
    Pipfile.lock  
    requirements.txt.lock  
    **/*.mypy_cache/

2. Visual Studio C++工程

    # 忽略编译生成的中间文件、输出文件等  
    *.obj  
    *.exe  
    *.ilk  
    *.lib  
    *.pdb  
    *.pch  
    *.idb  
    *.ipdb  
    *.user  
    *.aps  
    *.ncb  
    *.opt  
    *.suo  
    *.tlb  
    *.tlh  
    *.bak  
    *.exp  
    *.lib  
    *.sbr  
    *.pdb  
    *.ipch/  
    *.obj/  
    *.pch  
    *.vspscc  
      
    # 忽略 Visual Studio 解决方案和用户特定的文件  
    *.sln  
    *.suo  
    *.user  
    *.opensdf  
    *.sdf  
    *.cachefile  
    *.csproj.user  
    *.vcxproj.user  
      
    # 忽略自动生成的依赖项文件  
    *.dep  
      
    # 忽略 IntelliSense 生成的文件  
    *.i*  
      
    # 忽略 NuGet 包目录和文件  
    packages/  
    *.nupkg  
      
    # 忽略 bin 和 obj 目录（这些通常包含编译生成的文件）  
    bin/  
    obj/  
      
    # 忽略任何与调试相关的文件或目录  
    Debug/  
    Release/  
    x64/Debug/  
    x64/Release/  
    DebugPublic/  
    ReleasePublic/  
      
    # 忽略其他可能自动生成的文件或目录  
    Generated Files/  
      
    # 忽略其他个人或机器特定的文件  
    *.userosscache  
    *.browse*  
    .vs/  
      
    # 忽略某些可能包含敏感信息的文件  
    *.usersecrets  
      
    # 如果你使用 Git LFS，可以忽略 Git LFS 跟踪的文件  
    *.lfs


## 10. git差异比较
显示工作目录（可以直接编辑的文件们）与暂存区（git add -u）之间的差异：  
    git diff 

显示暂存区与最新提交之间的差异：  
    git diff --cached

## 11. 撤消git add操作
    如果没有commit，可以git resets，撤消暂存区修改  
    git checkout撤消工作修改  

## 12. 取消对文件的跟踪
如果你想取消对名为folder_to_untrack的文件夹的跟踪，可以使用以下命令：  
    git rm -r --cached folder_to_untrack

## 13. 删除以前的提交记录
创建一个没有父提交历史记录的孤立分支。这个命令实际上创建了一个新的分支，并且这个分支与以前的历史记录没有任何关联，因此会清空以前的历史记录。  

    git checkout --orphan  
具体来说，git checkout --orphan <branch_name>命令将创建一个新分支 <branch_name>，但是不会将它与任何先前的提交连接起来。这意味着该分支将不会继承任何历史记录，而只会包含当前工作目录中的文件。这可以用于开始一个全新的项目或者重写项目的历史记录。  

    git checkout --orphan new_branch_name  
    
添加当前状态到新创建的分支，这样新分支将包含你当前的所有文件。  

    git add -A  
    git commit -m "Initial commit"  
    
如果你想完全移除以前的历史记录，你可以删除之前的其他分支。  

    git branch -D old_branch_name  
    
如果你之前已经将代码推送到了远程仓库，你可能需要强制推送以覆盖远程仓库的历史记录。  

    git push origin new_branch_name --force

## 14. 忽略所有文件但除了某个文件以外

    # 忽略所有文件夹  
    */  
      
    # 但不忽略special-folder及其内容  
    !special-folder/  
    !special-folder/**/*

    # 例如
    # 第一级文件处理
    */
    # 第二级文件处理
    !opengl/
    !opengl/**/*
    !network/
    !network/**/*
    # 除了liushu这个文件夹之外 
    !liushu/
    # 但是先全部忽略
    liushu/*
    # 但不是忽略Test文件夹和目录，注意文件和文件夹都需要，同时，在*/后，liushu文件夹已经被忽略了，所以要加上这个
    !liushu/Test/
    
    # 第三级文件处理
    !liushu/Test/**/*
    !liushu/GrooveBox/
    !liushu/GrooveBox/**/*
