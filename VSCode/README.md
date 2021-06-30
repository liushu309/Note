### 1. 换行
  文件->首选项->设置->world warp

### 2. tab键跳出括号
  插件tabOut
  
### 3. 终端字太丑
    Terminal › Integrated: Font Family
    monospace

### 4. ubuntu进入函数后返回
Ctrl + Alt + -

### 5. vscode配置
主要在configurations中添加args变量,添加str列表,键与值都是str元素

        {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Python: 当前文件",
                    "type": "python",
                    "request": "launch",
                    "program": "${file}",
                    "args": [
                        "--net",
                        "res101",
                        "--cuda",
                        "--load_dir",
                        "models",
                        "--checksession",
                        "1",
                        "--checkepoch",
                        "2",
                        "--checkpoint",
                        "5010"
                    ],
                    "console": "integratedTerminal"
                }
            ]
        }
### 6. 生成c_cpp_properties.json
  Ctrl+Shift+P 打开命令 输入configuration 点第一个才有 c_cpp_properties.json
