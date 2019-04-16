### 1. keras限定内存和指定gpu型号
keras默认会占满gpu

    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    import tensorflow as tf
    from keras.backend.tensorflow_backend import set_session
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.5
    set_session(tf.Session(config=config))
