## 连接github
  1> sudo apt-get install openssh-server openssh-client
  2> sudo apt-get install git-core
  3> ssh-keygen -C '670602937@qq.com' -t rsa
  4> 默认生成的key在/home/.ssh/id_rsa.pub, 登录github-Account Settings-SSH Keys-Add SSH Key，title随意，粘贴SSH key
  5> git config --global user.name "your name"
     git config --global user.email "your email"
  6> 测试：ssh -v git@github.com
