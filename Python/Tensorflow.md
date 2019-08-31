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

## 6. 加载checkpoint
    import numpy as np
    ...
    
    config=tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.3
    sess = tf.Session(config=config)
    img_slot = tf.placeholder(tf.float32, shape=(1, 224, 224, 3))

    NUM_CLASS = 3
    
    graph_id_card_senet = tf.get_default_graph()
    with graph_id_card_senet.as_default():
      senet_network_fn = nets_factory.get_network_fn(
        "resnet_v2_50",
        num_classes=NUM_CLASS,
        is_training=False,
        attention_module="se_block")

      logits, end_points = senet_network_fn(img_slot)

      image_preprocessing_fn_senet = preprocessing_factory.get_preprocessing(
        'resnet_v2_50',
        is_training=False)

      saver = tf.train.Saver()

      try:
        last_checkpoint = tf.train.latest_checkpoint("models/checkpoints_idcard_senet")
        print(last_checkpoint)
        if last_checkpoint:
            saver.restore(sess, last_checkpoint)
      except:
        traceback.print_exc()

    id_card_senet_class_name = {
      0:'back',
      1:'front',
      2:'person',
    }

    def senet_eval_photo_classify(image):
      with graph_id_card_senet.as_default():
        res = {}
        image = image.resize([224, 224])
        image_array = np.array(image)
        if image_array.shape[-1] == 4:
            image_array = cv2.cvtColor(image_array, cv2.COLOR_RGBA2RGB)
        image_array = image_array.astype('float32')

        image_test = image_preprocessing_fn_senet(image_array, 224, 224)
        image_test = tf.expand_dims(image_test, 0)

        with sess.as_default():
            image_test = sess.run(image_test)
            x = end_points['predictions'].eval(feed_dict={img_slot: image_test})
        res['class_rate'] = str(x.max())
        res['class_num'] = str(x.argmax())
        res['class_name'] = id_card_senet_class_name[x.argmax()]
        return res
        
    if __name__ == "__main__":
        img_names = glob.glob(os.path.join(sys.argv[1], '*.jpg'))
        rets = []
        for img_name in img_names:
            print('deal img ', img_name)
            img = Image.open(img_name)
            ret = senet_eval_photo_classify(img)
            rets.append(ret)
        for ret in rets:
            print(ret)

## 7. 数据增强
Augmentor和imgaug,Augmentor使用比较简单,只有一些简单的操作。 imgaug实现的功能更多，可以对keypoint, bounding box同步处理，在segmentation和detection任务经常使用imgaug这个库。
### Augmentor
    # coding:utf-8
    import Augmentor
    import os

    path = os.path.abspath("1")
    print(path)
    p = Augmentor.Pipeline(path)

    p.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
    p.skew(probability=0.8, magnitude=0.1)
    p.shear(probability=0.8, max_shear_left=2, max_shear_right=2)
    p.zoom(probability=0.7, min_factor=0.8, max_factor=1.0)
    p.resize(probability=1.0, width=224, height=224)

    p.save_format="png"
    #p.process()
    p.sample(3000)


## 8. tf.Graph().as_default()
定义了一个新的图

    graph = tf.Graph()
    with graph.as_default():
        ...
所有的变量必须都在graph内，比如将tf.placeholder定义在graph外面，现所有的变量都会放到tf.get_default_graph()中，而不会出现在tf.Graph()，可能出现ValueError: No variables to save的错误

    img_slot = tf.placeholder(tf.float32, shape=(1, 224, 224, 3))
    graph = tf.Graph()
    with graph.as_default():
        ....
更改

    graph = tf.Graph()
    with graph.as_default():
        img_slot = tf.placeholder(tf.float32, shape=(1, 224, 224, 3))
        ....
