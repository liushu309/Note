## 1. 信号与槽
### 1. 主要有声明，连接，发送  
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
### 2. 当槽函数为自定义函数的时候
当槽函数为自定义的时候，类的声明必须继承QObject，而且类发声明中必须包含Q_OBJECT，如下：

    #include <QObject>
    
    class BaseClass:public QObject
    {
        Q_OBJECT
    public:
        BaseClass();
        virtual int baseVirtualFuction();
        virtual int basePureVirtual() = 0;
    };




## 2. Qt提升控件
Qt提升控件可以重载虚函数，比如用于OpenGL Widget

## 3. Qt多线程
1. Thread::quit():给程序一个退出的命令，但是对自定义的whild循环不起作用，while循环中还是在周期循环。  
2. Thread::wait():阻塞调用线程（比如主线程调用子线程），等待子线程run完。完是对while循环也是无效，反而在界面点x时，界面无响应。不过可以确保程序在退出以前线程有时间执行完毕，所以和while循环里的控制变量一起使用很好。  

    //.h
    protected:
        void closeEvent(QCloseEvent *event) override;
    
    // .cpp
    void MainWindow::closeEvent(QCloseEvent *event) {
        // 询问用户是否真的要关闭窗口
        QMessageBox::StandardButton reply;
        reply = QMessageBox::question(this, "信息",
            "要关了它，中文报错写英文?",
            QMessageBox::Yes|QMessageBox::No);
        if (reply == QMessageBox::Yes) {
    
            // 通过变量控制开关
            my_thread_1->stop_condition();
            my_thread_1->quit();
            // 阻塞主线程，避免主线程退了，子线程还没有退报错
            my_thread_1->wait();
            // 用户确认关闭窗口，调用基类的closeEvent来实际关闭窗口
            QWidget::closeEvent(event);
        } else {
            // 用户取消关闭窗口，忽略这个事件
            event->ignore();
        }
    }

3. QMutex  
定义共享资源  
首先，你需要定义你的共享资源。这可能是一个类的静态成员、全局变量、指针、容器或其他数据结构。确保这个资源在多个线程之间是可访问的。  

      // 都有线程使用的都是相同的mutex对象
      mutex.lock(); // 锁定互斥锁  
      // 在这里访问和修改共享资源  
      sharedGlobalVariable++; // 或 SharedResourceClass::sharedStaticMember++  
      mutex.unlock(); // 解锁互斥锁
   
注意：确保所有线程都使用相同的 QMutex 实例来锁定和解锁对共享资源的访问。  

5. QWaitCondition
6. 
    forever {  
        // 重点，下面这行必须有
        mutex.lock();  
        keyPressed.wait(&mutex);  
        do_something();  
        // 重点，下面这行必须有
        mutex.unlock();  
    }
   
mutex.lock();：首先，线程尝试获取互斥锁。如果锁已经被其他线程持有，则当前线程会阻塞，直到锁被释放。  
keyPressed.wait(&mutex);：一旦线程成功获取了互斥锁，它会调用 wait 函数，将互斥锁的所有权传递给 QWaitCondition 对象，并进入等待状态。此时，线程会释放互斥锁，并等待其他线程调用 keyPressed.wakeOne() 或 keyPressed.wakeAll() 来唤醒它。  
do_something();：只有当 keyPressed.wait(&mutex); 被其他线程通过 wakeOne() 或 wakeAll() 唤醒时，当前线程才会继续执行，并到达 do_something(); 这一行。如果没有其他线程唤醒它，do_something(); 将不会被执行。  
mutex.unlock();：在 do_something(); 执行完毕后，线程释放互斥锁。  
因此，当程序第一次执行到这个函数时，由于 keyPressed 还没有被其他线程唤醒，所以 do_something(); 将不会被执行。只有当另一个线程调用了 keyPressed.wakeOne() 或 keyPressed.wakeAll() 之后，当前线程才会被唤醒，并继续执行 do_something();。  


