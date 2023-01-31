### win10同时启动两个tomcat服务器  
1. 去除环境变量CATALINA_HOME和CATALINA_BASE环境变量，不去除的话，总是会去运行第一个配置好的tomcat程序，注意，PATH变量有可能会有%CATALINA_HOME%/bin的路径，也要删除；  
2. 修改conf/server.xml文件中的三个地方  


        # 第一处：<Server port="8005" shutdown="SHUTDOWN">
        <Server port="8006" shutdown="SHUTDOWN">

        # 第二处及第三处：<Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />
        # 注意这里的port8080最好往后加两个，如8082，可能和通讯有关，也不要加太多，如18080，可能计算机无法分资源。
        <Connector port="8082" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8446" />


### win10开关nginx
在“开关nginx.bat”文件中，写入如下代码：

        # 查看所有的nginx进程名称
        tasklist /fi "imagename eq nginx.exe"
        # 关闭所有的名称
        taskkill /f /t /im nginx.exe
