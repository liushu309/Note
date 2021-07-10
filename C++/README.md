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
	    # 写或许可以用fprintf
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
