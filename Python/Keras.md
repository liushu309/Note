## 1. keras限定内存和指定gpu型号
keras默认会占满gpu

    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    import tensorflow as tf
    from keras.backend.tensorflow_backend import set_session
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.5
    set_session(tf.Session(config=config))
    
## 2. keras自定义训练样例
    import keras.backend as K 
    import tensorflow as tf 
    import numpy as np 

    from keras.layers import Input, Conv2D, LeakyReLU, MaxPool2D
    from keras.models import Model

    from keras.optimizers import Adam

    x_data_0 = np.random.randn(100, 10, 10, 3) - 1
    y_0 = np.zeros(100)

    x_data_1 = np.random.randn(100, 10, 10, 3) + 1
    y_1 = np.ones(100)

    seed_factor = 1024

    x_data = np.vstack((x_data_0, x_data_1))
    y_data = np.hstack((y_0, y_1))

    y_data = y_data[:, np.newaxis, np.newaxis, np.newaxis]

    print(y_data.shape)
    
    np.random.seed(seed_factor)
    np.random.shuffle(x_data)
    np.random.seed(seed_factor)
    np.random.shuffle(y_data)

    limit_index = 160

    input_x = Input(shape = (10, 10, 3))
    x = Conv2D(4, (3, 3), padding = 'valid', strides = 2, name = 'liushu')(input_x)
    x = LeakyReLU(alpha = 0.1)(x)

    x = Conv2D(4, (1, 1), padding = 'same', strides = 1, name = 'the_same')(x)

    # x = Conv2D(2, (3, 3), padding = 'valid', strides = 2)(x)
    x = LeakyReLU(alpha = 0.1)(Conv2D(2, (3, 3), padding = 'valid', strides = 2)(x))

    y_pre = Conv2D(1, (1, 1))(x)

    model = Model(inputs = input_x, outputs = y_pre)
    model.compile(optimizer = Adam(lr = 1e-4), loss = 'mse', metrics=['accuracy'])
    model.fit(x_data[:limit_index], y_data[:limit_index], batch_size = 32, epochs = 10)


    json_string = model.to_json()
    file_write = open('./model_json.txt', 'w')
    file_write.write(json_string)
    file_write.close()

    for idx, layer in enumerate(model.layers):
        print('layer {}| : {}\n     layer name |{}'.format(idx, layer, layer.name))

    # model.save('./test.h5')

    print(x)
    print(x.shape)
    print(y_pre)
    print(y_pre.shape)
    # print(y.shape)


## keras处理不定长序列
### 1. 填充数据
pad_sequences

    X = pad_sequences(X, maxlen=int(self.max_frames), value=0.0, padding='post', dtype='float32')
### 2. 过滤
Masking

    model = Sequential()
    model.add(Masking(mask_value = 0,input_shape=self.input_shape))
    model.add(LSTM(2048, return_sequences=False,
                input_shape=self.input_shape,
                dropout=0.5))

