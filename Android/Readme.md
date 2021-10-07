## 1. 运行时权限
android6.0以上添加了运行时权限

## 2. AndroidManifest.xm文件
    //注意后面的camera是大写的,小
    <uses-permission android:name="android.permission.CAMERA">

## 3. SnackBar
    // 注意是先setContentView,再findViewByid,才能在SnackBar中使用,不然报
        setContentView(R.layout.activity_main);
        mLayout = findViewById(R.id.main_layout);

## 4. java环境配置
### 4.1 配置文件
    $vi ~/.bashrc
    134 # JAVA_HOME
    export JAVA_HOME=/usr/local/jdk1.8.0_291
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
    export PATH=$PATH:$JAVA_HOME/bin
    export PATH=$PATH:$JAVA_HOME/jre/bin
### 4.2 运行
    package com.example.lib;

    public class MyTestClass {
        public static void main(String[] args) {
            if(args != null){
                for(int i = 0;i<args.length;i++){
                    System.out.println("test"+args[i]);
                }
            }
            System.out.println("test");
        }
    }
    
    $ls-pc#:javac MyTestClass.java
    // 回退到上三层目录cd ../../..,不然找不到类
    $ls-pc#:java com.example.lib.MyTesstClass

### 4.3 Java环境搭建
编写Java文件:HelloMyJni.java  

    public class HelloMyJni{
        public native void helloWorld(); // 注意，这个native方法就是调用C语言接口用的
        static{
            System.loadLibrary("hello");  // 这行是调用动态链接库
        }
        public static void main(String[] args){
            new HelloMyJni().helloWorld();
        }
    }
    
编译Java文件并生成java头文件  

    javac -d . HelloMyJni.java // 生成主调用文件,注意:运行时java HelloMyJni, 后面不要加".class"  
    javah -jni HelloMyJni // 生成java头文件 com_hongyu_jni_HelloJni.h  

创建C语言文件，HelloWorld.c    

    #include "jni.h"
    #include "com_hongyu_jni_HelloJni.h"
    #include <stdio.h>
    #include <stdlib.h>

    JNIEXPORT void JNICALL Java_com_hongyu_jni_HelloJni_helloWorld(JNIEnv * env, jobject obj) 
        {

            printf("Hello World!\n");

        }

生成动态链接库文件 libhello.so   

    #gcc -Wall -fPIC -c HelloWorld.c -I ./ -I $JAVA_HOME/include/linux/ -I $JAVA_HOME/include/   
    #gcc -Wall -rdynamic -shared -o libhello.so HelloWorld.o  

执行  

    java HelloMyJni



## 5. android调用opencv
### 5.1 android调用C++
主要利用C++返回类对象指针，调用其它类成员函数时，使用指针函数调用类对象  
https://blog.csdn.net/xukaiup/article/details/88656558
### 5.2 andoird调用opencv
https://www.cnblogs.com/xiaoxiaoqingyi/p/6676096.html
