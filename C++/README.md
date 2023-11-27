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


### 3.3 typedef和宏

	#include <stdio.h>
	
	// 回调函数原型声明（名称为callback_func）和类型定义
	typedef void (*callback_func)(int);
	
	// 调用函数，接受一个回调函数作为参数
	void process(int data, callback_func callback)
	{
	    // 处理数据
	    printf("Processing data: %d\n", data);
	
	    // 调用回调函数
	    callback(data);
	}
	
	// 调用函数，接受一个回调函数作为参数
	void process_no_typedef(int data, void (*callback)(int))
	{
	    // 处理数据
	    printf("Processing no typedef data: %d\n", data);
	
	    // 调用回调函数
	    callback(data);
	}
	
	// 回调函数的实现
	void my_callback(int data)
	{
	    printf("Callback called with data: %d\n", data);
	}
	
	int main()
	{
	    // 调用process函数，并传递回调函数
	    process(10, my_callback);
	    // 调用process函数，并传递回调函数
	    process_no_typedef(20, my_callback);
	
	    return 0;
	}

	Processing data: 10
	Callback called with data: 10
	Processing no typedef data: 20
	Callback called with data: 20
 
用途：宏定义主要用于文本替换，而typedef主要用于定义数据类型。  

### 3.4 molloc和new的区别 

    malloc和new在内存分配和初始化方面存在一些显著的差异。
    内存分配方式：malloc在堆上进行内存分配，而new在自由存储区（free store）进行内存分配。自由存储区是C++中通过new和delete动态分配和释放对象的抽象概念。  
    初始化功能：malloc只负责开辟内存，没有初始化功能，需要用户自己初始化。而new不仅开辟内存，还可以进行初始化，例如，new int(10)表示在堆上开辟了一个4字节的int整形内存，初始值是10。  
    内存释放：malloc开辟的内存只能通过free来释放，而new开辟的内存，单个元素是使用delete来释放，如果new[]数组，则使用delete[]来释放。  
    效率：new是关键字，而malloc是库函数，因此new的效率可能高于malloc。  
    错误检测：对于内存泄漏，malloc无法明确指出是哪个文件的哪一行，而new则可以明确指出。  
    总的来说，malloc和new在内存分配、初始化、释放、错误检测以及效率方面都有各自的特点和差异。在编程时，需要根据实际需求和情况选择使用。  

    malloc和new都可以用于动态内存分配，但它们在C和C++中的使用方式有所不同。  
    
    在C语言中，我们通常使用malloc来分配内存。以下是一个基本的使用示例：  


	#include <stdlib.h>  
  
	int main() {  
	    int *ptr = (int*) malloc(sizeof(int));  // 分配一个int大小的内存空间  
	    if (ptr == NULL) {  
	        printf("Memory not allocated.\n");  
	        exit(0);  // 如果内存分配失败，程序退出  
	    } else {  
	        *ptr = 10;  // 在分配的内存中存储数据  
	        printf("Value of ptr: %d\n", *ptr);  // 打印存储的值  
	        free(ptr);  // 使用完毕后，释放内存  
	    }  
	    return 0;  
	}



    在C++中，我们通常使用new来分配内存。以下是一个基本的使用示例：  
    
	int main() {  
	    int *ptr = new int;  // 分配一个int大小的内存空间  
	    *ptr = 10;  // 在分配的内存中存储数据  
	    std::cout << "Value of ptr: " << *ptr << std::endl;  // 打印存储的值  
	    delete ptr;  // 使用完毕后，释放内存  
	    return 0;  
	}
 
    无论是malloc还是new，都需要进行内存释放操作。对于malloc分配的内存，我们使用free来释放；对于new分配的内存，我们使用delete来释放。  


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
    
    # 1. root开启(每个shell终端都要重新开启，如果不设置完局的话)
    ulimit -c unlimited 
    ＃ 设置后在ulimit -c 查看，结果为unlimited
    ulimit -c
    
    # 2. 以root用户写入
    root@ls-pc:echo  "core-%e-%p-%t" > /proc/sys/kernel/core_pattern
    #%e表示可执行程序
    #%p表示进程id
    #%t表示时间
    #这三个参数可加可不加

    3. 以root用户, 谱通用户可能需要重启，编译方式必须是-g, 而不是-c
    root@ls-pc:./a.out

    4. 在同目录下有core文件出现 
    root@ls-pc:gdb a.out core-....

    
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


