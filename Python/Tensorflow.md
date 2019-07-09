## 1. tensorboard 出现locale.Error: unsupported locale setting错误
  ### 终端
    liushu@ls-pc:~$locale
  ### 修改为空项
    export LANGUAGE=en_US.UTF-8
    export LC_ALL=en_US.UTF-8 

## 2. tf.while_loop()
将第三个参数依次放入cond中，根据结果判断是否执行body，如果执行完body后，将结果返回给变量，再次重复上述过程。cond和body的参数表必须相同，同时while_loop的返回值也与上述参数表一致。使用示例：  

    import tensorflow as tf 
    
    i = tf.constant(0)
    # 返回bool
    c = lambda i: tf.less(i, 10)
    # 加1
    b = lambda i: tf.add(i, 1)
    r = tf.while_loop(c, b, [i])

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        r_val = sess.run(r)
        print(r_val)
        
    out:
    10

## 3. TensorArray
TensorArray动态张量数组，通常都是跟while_loop或map_fn结合使用

    import tensorflow as tf

    def condition(time, output_ta_l):
        return tf.less(time, 3)

    def body(time, output_ta_l):
        output_ta_l = output_ta_l.write(time, [2.4, 3.5])
        return time + 1, output_ta_l

    time = tf.constant(0)
    output_ta = tf.TensorArray(dtype=tf.float32, size=10, dynamic_size=True)

    result = tf.while_loop(condition, body, loop_vars=[time, output_ta])

    last_time, last_out = result

    final_out = last_out.stack()

    with tf.Session():
        print(last_time.eval())
        print(final_out.eval())
    out:
    3
    [[2.4 3.5]
     [2.4 3.5]
     [2.4 3.5]]
     
### TensorArray.stack(name=None) 
将TensorArray中元素叠起来当做一个Tensor输出

## 4. 概念
### 4.1 with tf.Session() as sess:
方便释放sess中的资源，下面两种方式等价  

    # Using the `close()` method.
    sess = tf.Session()
    sess.run(...)
    sess.close()

    # Using the context manager.
    with tf.Session() as sess:
      sess.run(...)

### 4.2 只使用CPU
1. 使用tensorflow的 with tf.device('/cpu:0'):函数  
2. 使用tensorflow声明Session时的参数  

        # tensorflow
        import tensorflow as tf 
        sess = tf.Session(config=tf.ConfigProto(device_count={'gpu':0}))
    
        # keras 
        import tensorflow as tf
        import keras.backend.tensorflow_backend as KTF
        KTF.set_session(tf.Session(config=tf.ConfigProto(device_count={'gpu':0})))
    
3. 使用CUDA_VISIBLE_DEVICES命令行参数

        import os
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    
注：上述代码一定要放在import tensorflow或keras等之前，否则不起作用。

## 5. train完成不释放显存
将train(callback)放在一个子进程中执行  

    import multiprocessing
    ...
    p = multiprocessing.Process(target=training, args=(callback,))
    p.start()
    p.join()

