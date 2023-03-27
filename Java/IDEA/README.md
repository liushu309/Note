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

## 5. Java发送邮件
    package com.example.send_test;

    import org.springframework.boot.autoconfigure.SpringBootApplication;

    import java.io.File;
    import java.io.IOException;
    import java.util.*;
    import javax.mail.*;
    import javax.mail.internet.*;

    @SpringBootApplication
    public class SendTestApplication {
        public static void main(String[] args) throws MessagingException, IOException {

            // 发送邮箱和邮箱的授权码
            final String username = "wqkj7001@163.com";
            // 16位授权码
            final String password = "XXXXXXXXXXXXXXXX";

            Properties props = new Properties();
            props.put("mail.smtp.auth", "true");
            props.put("mail.smtp.host", "smtp.163.com");
            props.put("mail.smtp.ssl.protocols", "TLSv1.2");
            props.put("mail.smtp.ssl.ciphersuites", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256");

            // 25端口
    //        props.put("mail.smtp.starttls.enable", "true");
    //        props.put("mail.smtp.port", "25");
            // 465端口
            props.put("mail.smtp.starttls.enable", "false");
            props.put("mail.smtp.socketFactory.port", "465");
            props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
            props.put("mail.smtp.ssl.checkserveridentity", "false");

            Session session = Session.getInstance(props,
                    new javax.mail.Authenticator() {
                        protected PasswordAuthentication getPasswordAuthentication() {
                            return new PasswordAuthentication(username, password);
                        }
                    });

            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress("wqkj7001@163.com"));
            message.setRecipients(Message.RecipientType.TO,
                    InternetAddress.parse("670602937@qq.com"));
            // 标题
            message.setSubject("Test Email 2");
            // 内容
            message.setText("This is a test email. 25 真的 精简的邮件！");

            // 附件
            MimeBodyPart attachmentPart = new MimeBodyPart();
            attachmentPart.attachFile(new File("D:\\DownLoad\\ChromeDownload\\滴滴电子发票.pdf"));
            Multipart multipart = new MimeMultipart();
            multipart.addBodyPart(attachmentPart);
            message.setContent(multipart);
            // 附件中的文本
            MimeBodyPart textPart = new MimeBodyPart();
            textPart.setText("This is a test email with attachment.");
            multipart.addBodyPart(textPart);

            // 发送
            Transport.send(message);
            System.out.println("Email sent successfully.");
        }
    }
