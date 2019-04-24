## 1. tensorboard 出现locale.Error: unsupported locale setting错误
  ### 终端
    liushu@ls-pc:~$locale
  ### 修改为空项
    export LANGUAGE=en_US.UTF-8
    export LC_ALL=en_US.UTF-8 

## 2. tf.while_loop()
将第三个参数依次放入cond中，根据结果判断是否执行body，如果执行完body后，将结果返回给变量，再次重复上述过程？使用示例：  

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
