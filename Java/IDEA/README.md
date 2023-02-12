## Idea配置tomcat
### Tomcat与IDEA的关系
1. idea后端服务器也是Tomcat下面的一个提供功能的接口，这一点与前面html网页一样，只是idea是tomcat主要下提供业务操作功能的程序，而前端是tomcat下提供UI功能的程序，两者都由tomcat提供请求，而端口号各不相同。  
2. 管理idea的tomcat接收的请求可能主要来自于前端，直接来自于用户的情形可能是在调试的时候。而管理前面的tomcat接收的请求可能主要来自于用户。
