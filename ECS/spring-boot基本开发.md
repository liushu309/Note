# 基本开发
## 1. 配置两个地方
New Project -> Spring Initializr -> ... -> "打钩" Web/Spring Web -> ...
### 1.1 pom.xml文件中的依赖
    注意，对于java1.8，这里使用的是spring-boot.2.7.6，使用3.0.0以上的版本会报错
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.4.2</version>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>8.0.31</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>druid-spring-boot-starter</artifactId>
        <version>1.1.20</version>
    </dependency>
### 1.2 application.properties文件中配置数据库连接的依赖
    server.port=8080
    spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
    spring.datasource.driver-class-name=com.mysql.jdbc.Driver
    spring.datasource.url=jdbc:mysql://localhost:3306/mydb
    spring.datasource.username=root
    spring.datasource.password=123456
    mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl

## 2 总体文件结构
    └─com
        └─liushu
            └─wangquetrain
                ├─controller
                    └─RegisterManage.java
                ├─entity
                    └─Register.java
                ├─mapper
                    └─RegisterMapper.java
                └─WangQueTrainApplication.java


## 1. 创建实体(entity)
在xxxAplication.java同级目录下，创建文件夹（package）和对应的类名，注意最好类名为表名，成员属性为数据库表中字段名称，方便映射：  

    public class Register {
    public Long id;                     // 记录id
    public String name;                 // 用户名
    public String tel;                  // 电话号码
    ...

## 2. 创建映射Mapper接口
1. 创建Mapper接口，在后面使用自动注入的方式使用它，注意这里只是接口，不是创建一个java类，注意接口后还要写extends BaseMapper<Register>  

        @Mapper
        public interface RegisterMapper extends BaseMapper<Register> {
        }

2. 在WangQueTrainApplication.java类上方写入扫描路径  

        @SpringBootApplication
        @MapperScan("com.liushu.wangquetrain.mapper")
        public class WangQueTrainApplication {


## 3. 创建控制层(Controller)
在xxxAplication.java同级目录下，创建文件夹controller和对应的控制类，使用自动注入的方式，创建一个Register接口对象，再完成相关操作  

        @RestController      // 这个类是控制层的标注
        public class RegisterManage {
            @Autowired       // 自动注入数据，因为java创建不了接口，这里需要配置文件注入数据后能生成对像
            RegisterMapper registerMapper;
            @PostMapping("/updata")
            public int registeData(@RequestBody Register register){   // 注意，这里使用json传对象的话，就必须使用@RequestBode注解，其它的不需要，只要属性名和mysql字段名一致就好
                int result = registerMapper.insert(register);         // 使用mybatis-plus内置的方法insert记录，返回成功操作的个数
                return result;
            }
        }


## 常见错误
### 1. java: 警告: 源发行版 17 需要目标发行版 17
修改三个地方  
    
    pom.xml
    <properties>
        <java.version>8</java.version>
    </properties>
    
    File->Setting->Build,Execution,Deplyments->Java Compiler
    Target bytecode version
             8
    
    File-> Project Setting
       SDK 1.8

    更新maven仓库...

### 2. java: 无法访问org.springframework.boot.SpringApplication, 类文件具有错误的版本 61.0, 应为 52.0, 请删除该文件或确保该文件位于正确的类路径子目录中。
    
    spring3.0.0以上不支持jdk8，将spring-boot改成2.7.5
    pom.xml文件
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.5</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    
# 2. 接收上传文件与拦截器
## 2.1 接收文件
前端用postman进行测试，用body/form-data输入两个参数：file_name:liushu, f：（选择文件），注意参数名与函数参数名一致。
    
    package com.example.filter.controller;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.PostMapping;
    import org.springframework.web.bind.annotation.RestController;
    import org.springframework.web.multipart.MultipartFile;

    import javax.servlet.http.HttpServletRequest;
    import java.io.File;
    import java.io.IOException;

    @RestController
    public class FilterManager {
        @PostMapping("/updata")
        public String updata(String file_name, MultipartFile f, HttpServletRequest request) throws IOException {
            System.out.println("file_name");
            System.out.println(f.getContentType());
            System.out.println(f.getOriginalFilename());

    //        上传后，才文件放在临时文件夹：C:/Users/ls/AppData/Local/Temp/tomcat-docbase.8080.5450699450388427383/upload
    //        http://localhost:8080/upload/1.webp可以访问图片
    //        spring.mvc.static-path-pattern=/**
    //        http://localhost:8080/image/upload/1.webp才可以访问图片
            String save_path = request.getServletContext().getRealPath("/upload/");
            // 注意：这里的路径和src/resources/static路径不在同一个地方，部署以后，虽然访问图片路径分别是
            // http://localhost:8080/image/upload/1.webp 上传后浏览器访问
            // http://localhost:8080/image/2.webp  后端之前放置的图片src/resources/static/2.webp
            // 但是相同的网络访问路径，并不代表两张图片路径相同部分代表相同的物理路径：http://localhost:8080/image
            // 后端中的static文件夹中的文件可能被打包到jar中去了
            System.out.println(save_path);
            saveFile(f, save_path);
            return "上传成功";
        }

        public void saveFile(MultipartFile f, String save_path) throws IOException {
            File dir = new File(save_path);
            if(!dir.exists()){
                dir.mkdir();
            }

            File file = new File(save_path + f.getOriginalFilename());
            f.transferTo(file);
        }

        @GetMapping("/updata")
        public String updateGet(){
            return "is ok!";
        }

        @GetMapping("/image/sea")
        public String imageSea(){
            return "this is the sea!";
        }
    }

## 2.2 拦截器  
需要进行拦截器的定义和注册两部  
### 2.2.1 拦截器定义  
完成接口HandlerInterceptor中的三个函数：preHandle（拦截前）、postHandle（拦截后）、afterCompletion（前端渲染后）即可：  
    
    package com.example.filter.controller;

    import org.springframework.web.servlet.HandlerInterceptor;
    import org.springframework.web.servlet.ModelAndView;

    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;

    public class FilterController1 implements HandlerInterceptor {
        @Override
        public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
            HandlerInterceptor.super.postHandle(request, response, handler, modelAndView);
            System.out.println("/image/**     postHandle accessed ");
        }

        @Override
        public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
            HandlerInterceptor.super.preHandle(request, response, handler);
            System.out.println("/image/**     preHandle accessed");
            return true;
        }

        @Override
        public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
            HandlerInterceptor.super.afterCompletion(request, response, handler, ex);
            System.out.println("/image/**     afterCompletion accessed");
        }
    }

类似有FilterController2类的定义，只是定义打印内容为"/image/sea/**"，其它不变：
    
    package com.example.filter.controller;

    import org.springframework.web.servlet.HandlerInterceptor;
    import org.springframework.web.servlet.ModelAndView;

    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;

    public class FilterController2 implements HandlerInterceptor {
        @Override
        public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
            HandlerInterceptor.super.postHandle(request, response, handler, modelAndView);
            System.out.println("/image/sea/** postHandle accessed");
        }

        @Override
        public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
            HandlerInterceptor.super.preHandle(request, response, handler);
            System.out.println("/image/sea/** preHandle accessed");
            return true;
        }

        @Override
        public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
            HandlerInterceptor.super.afterCompletion(request, response, handler, ex);
            System.out.println("/image/sea/** afterCompletion accessed");
        }
    }

### 2.2.2 拦截器的注册
主要完成接口WebMvcConfigurer，在addInterceptors方法中进行注册：

    package com.example.filter.controller;

    import org.springframework.stereotype.Controller;
    import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
    import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

    @Controller
    public class ConfigController implements WebMvcConfigurer {
        @Override
        public void addInterceptors(InterceptorRegistry registry) {
            WebMvcConfigurer.super.addInterceptors(registry);

            registry.addInterceptor(new FilterController1()).addPathPatterns("/image/**");
            registry.addInterceptor(new FilterController2()).addPathPatterns("/image/sea/**");
        }
    }

使用上面接收文件的FilterManager类，run一下：
    

    2023-04-03 21:01:58.010  INFO 7416 --- [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing ...
    2023-04-03 21:01:58.012  INFO 7416 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet ...
    2023-04-03 21:01:58.016  INFO 7416 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 3 ms
    /image/**     preHandle accessed
    /image/sea/** preHandle accessed
    /image/sea/** postHandle accessed
    /image/**     postHandle accessed
    # === 后端返回给前端，前端渲染后
    /image/sea/** afterCompletion accessed
    /image/**     afterCompletion accessed    

    
