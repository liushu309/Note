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
  
### 7. 配置java环境
    1. 先安装Language Support for Java(TM) 0.64.1版本的，再装Java Extension Pack
    2. Ctrl + ","，输入javahome，配置如下：
    
    "java.home": "/usr/local/jdk1.8.0_291",
    "java.requirements.JDK11Warning": false,
    "java.semanticHighlighting.enabled": true
    
### 8. 调试opencv
主要配置task.json文件 

    {
        "tasks": [
            {
                "type": "cppbuild",
                "label": "C/C++: g++ 生成活动文件",
                "command": "/usr/bin/g++",
                "args": [
                    "-g",
                    "${file}",
                    "${fileDirname}/WifiBlueToothLocation.cpp",
                    "-o",
                    "${fileDirname}/${fileBasenameNoExtension}",
                    "-I",
                    "/usr/local/opencv_3.4.15/include/opencv",
                    "-I",
                    "/usr/local/opencv_3.4.15/include/opencv2",
                    "-I",
                    "/usr/local/opencv_3.4.15/include",
                    "-L",
                    "/usr/local/opencv_3.4.15/lib",
                    "-l",
                    "opencv_dnn",
                    "-l",
                    "opencv_saliency",
                    "-l",
                    "opencv_reg",
                    "-l",
                    "opencv_optflow",
                    "-l",
                    "opencv_calib3d",
                    "-l",
                    "opencv_bgsegm",
                    "-l",
                    "opencv_highgui",
                    "-l",
                    "opencv_videostab",
                    "-l",
                    "opencv_fuzzy",
                    "-l",
                    "opencv_stereo",
                    "-l",
                    "opencv_videoio",
                    "-l",
                    "opencv_line_descriptor",
                    "-l",
                    "opencv_shape",
                    "-l",
                    "opencv_stitching",
                    "-l",
                    "opencv_tracking",
                    "-l",
                    "opencv_dnn_objdetect",
                    "-l",
                    "opencv_imgcodecs",
                    "-l",
                    "opencv_objdetect",
                    "-l",
                    "opencv_bioinspired",
                    "-l",
                    "opencv_text",
                    "-l",
                    "opencv_aruco",
                    "-l",
                    "opencv_xobjdetect",
                    "-l",
                    "opencv_rgbd",
                    "-l",
                    "opencv_face",
                    "-l",
                    "opencv_core",
                    "-l",
                    "opencv_ximgproc",
                    "-l",
                    "opencv_hdf",
                    "-l",
                    "opencv_datasets",
                    "-l",
                    "opencv_superres",
                    "-l",
                    "opencv_freetype",
                    "-l",
                    "opencv_flann",
                    "-l",
                    "opencv_hfs",
                    "-l",
                    "opencv_surface_matching",
                    "-l",
                    "opencv_structured_light",
                    "-l",
                    "opencv_photo",
                    "-l",
                    "opencv_imgproc",
                    "-l",
                    "opencv_ml",
                    "-l",
                    "opencv_features2d",
                    "-l",
                    "opencv_phase_unwrapping",
                    "-l",
                    "opencv_video",
                    "-l",
                    "opencv_xfeatures2d",
                    "-l",
                    "opencv_dpm",
                    "-l",
                    "opencv_ccalib",
                    "-l",
                    "opencv_plot",
                    "-l",
                    "opencv_img_hash",
                    "-l",
                    "opencv_xphoto",
                ],
                "options": {
                    "cwd": "${fileDirname}"
                },
                "problemMatcher": [
                    "$gcc"
                ],
                "group": {
                    "kind": "build",
                    "isDefault": true
                },
                "detail": "调试器生成的任务。"
            }
        ],
        "version": "2.0.0"
    }

获取函数如下：

    import os
    import sys


    def getLibGDBTaskInfo(input_lib_root, output_file):

        # 获取opencv include目录
        text_include_str = ""
        include_dir = os.path.join(input_lib_root, "include")
        include_dir_items = os.listdir(include_dir)
        include_list = [os.path.join(include_dir, sub_dir)
                        for sub_dir in include_dir_items]
        include_list.append(include_dir)
        for line in include_list:
            temp = f'"-I", "{line}",\n'
            text_include_str += temp
        # # print(include_list)
        # # print(text_include_str)

        # 获取opencv libs目录
        lib_dir = os.path.join(input_lib_root, "lib")
        lib_items = os.listdir(lib_dir)
        text_lib_path_str = f'"-L", "{lib_dir}",\n'
        # print(text_lib_path_str)

        text_lib_str = ""
        for lib_name in lib_items:
            # # print(lib_name)
            if lib_name.endswith(".so"):
                # print(lib_name, "<====")
                lib_short_name = lib_name[3:-3]
                # print(lib_short_name)
                temp = f'"-l", "{lib_short_name}",\n'
                text_lib_str += temp
        # print(text_lib_str)

        # 合并
        all_string = text_include_str + text_lib_path_str + text_lib_str
        with open(output_file, "w") as f:
            f.write(all_string)


    if __name__ == "__main__":

        input_lib_root = "/usr/local/opencv_3.4.15"
        output_file = "./opencv_task.txt"
        # getLibGDBTaskInfo(sys.argv[1], sys.argv[2])
        getLibGDBTaskInfo(input_lib_root, output_file)


### 9. 在vscode中加入git-bash终端
1. 设置  
2. settings.json
3. 添加设置，代码如下：


      {
          "terminal.integrated.profiles.windows": {
              "Git-Bash": {
                  "path": "D:\\SoftWare\\git\\bin\\bash.exe",
                  "args": [],
                  "icon": "terminal-bash"
              },
           },
          "terminal.integrated.defaultProfile.windows": "Git-Bash",
      }
