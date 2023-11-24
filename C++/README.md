## 1. C++格式华生成字符串变量
	#include <iostream>
	#include <stdio.h>

		int main(){
		    int a = 100;
		    char str[40];
		    sprintf(str, "the input number is %04d.jpg", a);
		    std::cout << "the product number is " << str << std::endl;
		    return 0;
		}

## 2. 读取文件
	#include <stdio.h>
	#include <iostream>
	#include <vector>
	#include <string.h>
	int main(int argc, const char *argv[])
	{
	    // 写或许可以用fprintf
	    FILE *f_obj = fopen("data/label.txt", "r");
	    char img_dir[128], label[32];
	    std::vector<std::string> imgs, labels;
	    while (!feof(f_obj))
	    {
		fscanf(f_obj, "%s %s\n", img_dir, label);

		imgs.push_back(std::string(img_dir));
		labels.push_back(std::string(label));
	    }

	    for (int i = 0; i < imgs.size(); i++)
	    {
		std::cout << imgs[i] << " " << labels[i] << std::endl;
	    }
	    return 0;

	    // 也可以使用fstream和getline读取一行
	    fstream f("dictionary.txt"); //创建一个fstream文件流对象
	    vector<string> words;        //创建一个vector<string>对象
	    string line;                 //保存读入的每一行
	    while (getline(f, line))     //会自动把\n换行符去掉
	    {
		words.push_back(line);
		cout << "----->   " << line << endl;
	    }
	    
	    
	    // 再使用stringstream对字符串进行拆分 
	    // 注意一定要#include <sstream>
	    string info = "12 43 43 543";
            stringstream ss_info(info);
	    // sstream会自动对数据类型进行转换，
	    int x, y, w, h;
	    // ss_info >> x;
	    // ss_info >> y;
	    // ss_info >> w;
	    // ss_info >> h;
	    ss_info >> x >> y >> w >> h;



	}

## 3. 概念
### 3.1 int * ptr与(int *) ptr
  int * ptr只是普通的指针声明，而(int *) prt有将ptr指什进行一个强制类型转换的意义？？？
### 3.2 int a[] = {1, 2, 3, 4, 5}与int *p = &a[0]
  虽然*a与*p以及*(a + 1)与*(p + 1)指向的结果都相同，但是a毕竟是数组名，猜测(*a)只是重载了a指针指向数组第一个元素，毕意sizeof(a)/sizeof(a[0]) == 数组长度，而sizeof(a[0])/sizeof(a[0]) == 1，所以认为a是一个结构体类型的对象，而int * p的声明中，p才是基本类型，比如下例：
    
    printf("*p = %d, *q = %d\n", *p, *q);
    printf("*(p+1) = %d, *(q+1) = %d\n", *(p+1), *(q+1));
    printf("**(&a + 1) value is %d\n", **(&a + 1));
    [out]
    *p = 1, *q = 1
    *(p+1) = 2, *(q+1) = 2
    **(&a + 1) value is 32764
    
  这里考虑的就是a[]中的a应该是数组名类型，而a+1当然指针的话，应该指的下一个数组，而不是下一个.

## 4. gdb调试
## 常用的命令
    break, run, print expr, c, next, edit, list, step, quit  

### 1. 编译
    g++ -g(重点不是-c) main.c

### 2. 开始调试 
    gdb ./a.out

### 3. 浏览代码
    l(显示10行代码)

### 4. 打断点
    b 10(在第10行的地方打断点)

### 5. 跑起来
    r(在断点的地方停下来)

### 6. 单步调试
    n(前进一步)

### 7. 进入函数体内部
    s

### 8. 打印数值
    print i(变量名，还可以是&i, *i)

### 9. 跳到下一个断点去
    c(contune)

### 10. 查看函数信息
    edit main(函数名)


### 4.1 ubuntu开启core文件
    
    # 1. 开启
    ulimit -c unlimited 
    ＃ 设置后在ulimit -c 查看，结果为unlimited
    ulimit -c
    # 以root用户写入
    root@ls-pc:echo  "core-%e-%p-%t" > /proc/sys/kernel/core_pattern
    #%e表示可执行程序
    #%p表示进程id
    #%t表示时间
    #这三个参数可加可不加
    
### 4.2 gdb调试正在运行的程序
以root用户进行调试，并且需要多n或者s几下，因为运行的程序可能也有其它的内容，不只是程序代码

	sudo gdb -p 1234(进程号)

	62	../sysdeps/posix/sleep.c: 没有那个文件或目录.
	(gdb) n
	64	in ../sysdeps/posix/sleep.c
	(gdb) n
	test1 () at error.cpp:12
	12	  i++;


## 5 报错信息
### 5.1 fatal error: string: 没有那个文件或目
将源文件的后缀名由.c改为.cpp


