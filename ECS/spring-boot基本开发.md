## 1. 配置两个地方
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



    
