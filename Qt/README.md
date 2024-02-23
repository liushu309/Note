## 1. 信号与槽
主要有声明，连接，发送  
### Qt4
声明  
信号：singnals(相当于public):函数名（参数类型，不加参数名），只声明，不定义
槽：（public,private,procte之一） slots:函数名（参数），要定义  
连接  
connets(SINGNALS(函数名（参数）），this(发送方），SOLT(函数名（参数）），this?）  
发送  
emit 信息函数（参数）
###  Qt5
声明  
信号：singnals(相当于public):函数名（参数类型，不加参数名），只声明，不定义
槽：一般的成员函数都可以  
连接  
connets(&类名::函数名（参数），this(发送方），&类名::函数名（参数），this?）  
发送  
emit 信息函数（参数）
