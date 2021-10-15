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

