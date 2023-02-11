### 1. 设置端口号
Proxy->Proxy Settings, Port:8888；  
### 2. 访问控制
Proxy->Access Control Settings, 点击Add，输入ip地址（可能是允许局域网内其它客户端访问）；
### 3. windows代理配置
win设置->网络和Internet->代理->使用代理服务器->......->保存（或许也是代理软件不在本地计算机上才使用）；
### 4. android代理配置
设置->WLAN->修改网络；
### 5. windows证书安装（抓取https报文）
help->SSL Proxying->Install Charles Root Certificate->安装证书->本地计算机->下一步->将所有证书都存放下列存储->浏览->受信任的根证书颁发机构->确定->下一步->完成；
### 6. http代理配置
Proxy->SSL proxying setting->Enable SSL Proxying->Add->Prot:443(Ip不管它)->OK;
### 7. 网页断点
在对应的网页上点击鼠标右键->breakpoint，在消息进会停，修改了报文后，再点击execute可以将消息推送出去。
