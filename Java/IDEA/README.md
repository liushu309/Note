## 1. Tomcat与IDEA的关系
1. idea后端服务器也是Tomcat下面的一个提供功能的接口，这一点与前面html网页一样，只是idea是tomcat主要下提供业务操作功能的程序，而前端是tomcat下提供UI功能的程序，两者都由tomcat提供请求，而端口号各不相同；  
2. 管理idea的tomcat接收的请求可能主要来自于前端，直接来自于用户的情形可能是在调试的时候。而管理前面的tomcat接收的请求可能主要来自于用户；  
3. 一般不需要在服务端单独配置tomcat，idea里面已经集成了，前端才需要。
## 2. 打包
点击maven->package，生成的jar包出现在[project_name]/target/***.jar

## 3. 部署后运行jar文件

  nohup java -jar filename-0.0.1-SNAPSHOT.jar > log.file 2>&1 &

## 4. 跨域问题
这个问题主要在服务端进行设置，在Controller类的方法上面，加@CrossOrigin，如下：  

    @RestController
    public class RegisterManage {
        @Autowired
        RegisterMapper registerMapper;
        @CrossOrigin
        @PostMapping("/updata")
        public int registeData(@RequestBody Register register){
            int result = registerMapper.insert(register);
            return result;
        }
    }