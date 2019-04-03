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
