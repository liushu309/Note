## 1. 信号与槽
主要有声明，连接，发送  
### Qt4
声明  
信号：singnals(相当于public):函数名（参数类型，不加参数名），只声明，不定义
槽：（public,private,procte之一） slots:函数名（参数），要定义  
连接  
connect(sender,SIGNAL(signal),receiver,SLOT(slot)，Qt::DirectConnection);  
连接通常在对象的构造函数中进行，但并非必须如此。  
发送  
emit 信息函数（参数）
###  Qt5
声明  
信号：singnals(相当于public):函数名（参数类型，不加参数名），只声明，不定义
槽：一般的成员函数都可以  
连接  
connect(sender, &SenderClass::signalName, receiver, &ReceiverClass::slotName);  
发送  
emit 信息函数（参数）
注意：  
1. 信号与槽在connect中的写法，都是写函数名，而不是写函数调用（即后面不要加参数）
2. 使用自定义的方法，就在头文件中去掉SOLT private:，因为它有可能会自己产生一个信号与槽函数，加上自己连的，一共执行两次槽函数。  



## Qt提升控件
Qt提升控件可以重载虚函数，比如用于OpenGL Widget