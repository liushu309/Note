## 1.1 python书写
主要使用的是opencv的FileStorage类写yaml, 在字典里写list, python的格式，会写一个fs.startWriteStruct("list_name", cv2.FileNode_SEQ), 会自己加一个名称，刚好和字典形式符合，但是在list里写dict的时候，也必须使用fs.startWriteStruct("dict_name", cv2.FileNode_MAP), 也即加一个名字，但是就是加了，也不符合list嵌套map的格式，如下：

    # map{list}
    first_dice:
    liushu: 777
    xinqiji: 777
    my_list:
        - 1
        - 2
        - 3

    # list(map)
    list:
    - first_item
    - FileNode_SEQ # 这个名称本意是创建map，但不是得不加一个名称，结果map的对象名和内容都成了list的一个元素
    -
        sub_dict_1: 1
        sub_dict_2: 123
    - xinqiji

  所以opencv-python只适合写一级格式的文件，不适合写多级的。

  yaml有行内书写，如下：

    # 两种写法等效
    liushu:[1, 3, 4]
    liushu:
        - 1
        - 3
        - 4


### 1.1.1 书写普通变量
    self.yaml_ob = cv2.FileStorage(yaml_dir, cv2.FileStorage_WRITE)
    # 一个对象在写
    self.yaml_ob.write("total_num", self.idx)

    # 效果
    total_num: 2160


### 1.1.2 字典和列表

    # 一个对象在写
    self.yaml_ob.startWriteStruct("label_range", cv2.FileNode_MAP)
    for label, idx in self.label_start_idx:
        self.yaml_ob.startWriteStruct(label, cv2.FILE_NODE_SEQ)
        self.yaml_ob.write("", idx)
        self.yaml_ob.write("", idx + self.angle_range - 1)
        self.yaml_ob.endWriteStruct()
    self.yaml_ob.endWriteStruct()

    ＃ 效果如下
    label_range:
        c:
            - 0
            - 359
        a:
            - 360
            - 719
        d:
            - 720
            - 1079
        e:
            - 1080
            - 1439
        b:
            - 1440
            - 1799
        f:
            - 1800
            - 2159


### 1.1.3 使用python模块yaml
  使用yaml模块，可以解决不同类型的嵌套问题

    import yaml
    import os

    class YamlObject():
        def __init__(self):
            self.dict = {}
            self.list = []
        def setDict(self, dict_object):
            self.dict = dict_object
        def setList(self, list_object):
            self.list = list_object


    def generate_yaml_doc(yaml_file):
        file = open(yaml_file, 'w', encoding='utf-8')
        yaml_dict = {"赵钱孙李": 7777, "xinqiji": 66666,
                    "good": [1, 3, 4, 51, "hello"]}
        yaml_list = [1, 3, 4, 4, "liuxuande", {"liushu": 777, "tangxuanzang": 666}]
        yaml_ob = YamlObject()
        yaml_ob.setDict(yaml_dict)
        yaml_ob.setList(yaml_list)
        yaml.dump(yaml_ob, file)
        file.close()

  输出

    !!python/object:__main__.YamlObject
    dict:
        good:
        - 1
        - 3
        - 4
        - 51
        - hello
        xinqiji: 66666
        "\u8D75\u94B1\u5B59\u674E": 7777
    list:
    - 1
    - 3
    - 4
    - 4
    - liuxuande
    - liushu: 777
      tangxuanzang: 666



## 1.2 读取
文件如下：

    %YAML:1.0
    ---
    wifi-id_mac_SSID:
    id_0:
        - "0c:4b:54:4d:e6:64"
        - wxzh_5G
    id_1:
        - "34:36:54:f7:38:4a"
        - ChinaNet-uhRzDf-5G
    id_2:
        - "ec:f0:fe:6c:c7:84"
        - ChinaNet-jtgQ

    yaml_file_ob = cv2.FileStorage("./liushu.yaml", cv2.FileStorage_READ)

    for i in range(3):
        print(f"the id is id_{i}")
        key = "wifi-id_mac_SSID"
        node = yaml_file_ob.getNode(key)
        # 读取列表
        ret = node.getNode(f"id_{i}").at(0)
        # 读取字典的话，直接(int(node.real())), (string(node.string()))
        print(node.real())

## 2 C++读写
  字典里的键所对应的值，如果是列表，（！必须）不写对象名，把键当成是对象名就可以了。列表里的元素，如果是字典，（！也必须）不写对象名，写了也会当成列表的一个元素。访问的时候就通过迭代器访问，而不是节点名（对象名）访问。

    #include <opencv2/core.hpp>
    #include <iostream>
    using namespace cv;
    using std::cout;
    using std::endl;
    using std::ostream;
    template <typename T>
    FileStorage &operator,(FileStorage &out, const T &data)
    {
        out << data;
        return out;
    }
    template <typename T>
    ostream &operator,(ostream &out, const T &data)
    {
        out << data;
        return out;
    }
    int main()
    {
        //write
        {
            FileStorage storage("file.yaml", FileStorage::WRITE);
            storage << "matrix", (Mat_<float>(2, 2) << 1, 2, 3, 4),
                "int", 1,
                "double", 2.2,
                "strings", "[:", "123", "456", "end", "]",
                "features", "[:";
            for (int i = 0; i < 3; ++i)
            {
                storage << "{:",
                    "x", i,
                    "y", i * i,
                    "lb", "[:";
                for (int j = 0; j < 4; ++j)
                {
                    storage << j;
                }
                storage << "]"
                        << "}";
            }
            storage << "]";
        }
        //read
        {
            FileStorage storage("file.xml", FileStorage::READ);
            cout << "matrix:", storage["matrix"].mat(), '\n',
                "int:", storage["int"].real(), '\n',
                "double:", storage["double"].real(), '\n';
            cout << "strings:";
            for (const auto &iter : storage["strings"])
            {
                cout << iter.string(), ',';
            }
            cout << endl;
            cout << "features:" << endl;
            for (const auto &iter : storage["features"])
            {
                cout << "-  {",
                    "x:", iter["x"].real(), ",",
                    "y:", iter["y"].real(), ",",
                    "lb:[";
                for (const auto &lbIter : iter["lb"])
                {
                    cout << lbIter.real(), ",";
                }
                cout << "]}\n";
            }
        }
        return 0;
    }
