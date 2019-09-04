from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import math
import os
import random
import sys
import tensorflow as tf
import argparse


# Seed for repeatability.
_RANDOM_SEED = 0

# The number of shards per dataset split.
_NUM_SHARDS = 4

LABELS_FILENAME = 'labels.txt'

# train, valid, test
division_ratio = [0.8, 0., 0.2]

# is force delete the temp foder
is_del_temp_foder = False
# is ignore the exists dataset folder
is_ignore_exists_folder = True
# return http error
is_return_http_err = False

def data_set_classification(data_path, temp_path):
    status = 2
    msg = ''
    
    abs_src_dir = os.path.abspath(data_path)  
    abs_temp_dir = os.path.abspath(temp_path)
    
    if not os.path.exists(abs_src_dir):
        msg = 'src dataset "%s" is not exists!'%(abs_src_dir)
        return 1, msg
        
    if not os.path.exists(abs_temp_dir):
        print('the process make the new dir "%s"!'%(abs_temp_dir))
        os.mkdir(abs_temp_dir)
    else:
        if is_del_temp_foder:
            shutil.rmtree(abs_temp_dir)
            os.mkdir(abs_temp_dir)
            print('old dir "%s" is delete, the new one is created!'%(abs_temp_dir))
        elif is_ignore_exists_folder:
            train_dir_name = os.path.join(abs_temp_dir, 'train_sample')
            test_dir_name = os.path.join(abs_temp_dir, 'test_sample')
            valid_dir_name = os.path.join(abs_temp_dir, 'valid_sample')
            is_train_exists = os.path.exists(train_dir_name)
            is_test_exists = os.path.exists(test_dir_name)
            is_valid_exists = os.path.exists(valid_dir_name)
            print('founding the old dataset folder: "%s"' % (abs_temp_dir))
            is_all_exists = is_train_exists and is_test_exists and is_valid_exists
            if is_all_exists:
                print('founding the old sub dataset folder: \n"%s"\n"%s"\n"%s", assume it already contain the train, test, valid dataset' % (train_dir_name, test_dir_name, valid_dir_name))
                return status, msg
            else:
                # msg = 'Error: some sub dataset missing:\n%s \n%s \n%s' % (
                #         'train found, %s' % str(is_train_exists), 
                #         'test found, %s' % str(is_test_exists),
                #         'valid found, %s' % str(is_valid_exists),
                #     )
                # print(msg)
                # return 1, msg
                if is_train_exists: shutil.rmtree(train_dir_name)
                if is_test_exists: shutil.rmtree(test_dir_name)
                if is_valid_exists: shutil.rmtree(valid_dir_name)
        else:
            msg = 'the dst temp folder "%s" is already exsits, please input a new one!' % (abs_temp_dir)
            status = 1
    
            return status, msg
        
    
    # 获取分类
    class_name = os.listdir(abs_src_dir)

    # 创建对应子集 train, valid, test
    train_dir_name = os.path.join(abs_temp_dir, 'train_sample')
    if not os.path.exists(train_dir_name):
        os.mkdir(train_dir_name)
    valid_dir_name = os.path.join(abs_temp_dir, 'valid_sample')
    if not os.path.exists(valid_dir_name):
        os.mkdir(valid_dir_name)
    test_dir_name = os.path.join(abs_temp_dir, 'test_sample')
    if not os.path.exists(test_dir_name):
        os.mkdir(test_dir_name)


    for idx in range(len(class_name)):
        class_dir = os.path.join(abs_src_dir, class_name[idx])
        class_list = os.listdir(class_dir)
        random.shuffle(class_list)
        
        train_limit = round(len(class_list) * division_ratio[0])
        valid_limit = round(len(class_list) * division_ratio[1])
        
        # 复制文件 src/class -> temp/class/train   
        train_class_path = os.path.join(train_dir_name, class_name[idx])
        if not os.path.exists(train_class_path):
            os.mkdir(train_class_path)
        for item in class_list[:train_limit]:
            src_file_name = os.path.join(abs_src_dir, class_name[idx], item)
            dst_file_name = os.path.join(train_class_path, item)
            shutil.copy(src_file_name, dst_file_name)
            
        # 复制文件 src/class -> temp/class/valid   
        valid_class_path = os.path.join(valid_dir_name, class_name[idx])
        if not os.path.exists(valid_class_path):
            os.mkdir(valid_class_path)
        for item in class_list[train_limit:train_limit + valid_limit]:
            src_file_name = os.path.join(abs_src_dir, class_name[idx], item)
            dst_file_name = os.path.join(valid_class_path, item)
            shutil.copy(src_file_name, dst_file_name)
            
        # 复制文件 src/class -> temp/class/train   
        test_class_path = os.path.join(test_dir_name, class_name[idx])
        if not os.path.exists(test_class_path):
            os.mkdir(test_class_path)
        for item in class_list[train_limit + valid_limit:]:
            src_file_name = os.path.join(abs_src_dir, class_name[idx], item)
            dst_file_name = os.path.join(test_class_path, item)
            shutil.copy(src_file_name, dst_file_name)  
            
    return status, msg



def int64_feature(values):
    if not isinstance(values, (tuple, list)):
        values = [values]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=values))


def bytes_feature(values):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))


def float_feature(values):
    if not isinstance(values, (tuple, list)):
        values = [values]
    return tf.train.Feature(float_list=tf.train.FloatList(value=values))


def image_to_tfexample(image_data, image_format, height, width, class_id):
    return tf.train.Example(features=tf.train.Features(feature={
        'image/encoded': bytes_feature(image_data),
        'image/format': bytes_feature(image_format),
        'image/class/label': int64_feature(class_id),
        'image/height': int64_feature(height),
        'image/width': int64_feature(width),
    }))


def write_label_file(labels_to_class_names, dataset_dir,
                     filename=LABELS_FILENAME):
    labels_filename = os.path.join(dataset_dir, filename)
    with tf.gfile.Open(labels_filename, 'w') as f:
        for label in labels_to_class_names:
            class_name = labels_to_class_names[label]
            f.write('%d:%s\n' % (label, class_name))


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_sample_dir", required=True)
    parser.add_argument("--valid_sample_dir", required=True)
    parser.add_argument("--test_sample_dir", required=True)
    parse_args = parser.parse_args()
    args = vars(parse_args)
    return args


class ImageReader(object):
    def __init__(self):
        # Initializes function that decodes RGB JPEG data.
        self._decode_jpeg_data = tf.placeholder(dtype=tf.string)
        self._decode_jpeg = tf.image.decode_jpeg(self._decode_jpeg_data, channels=3)

    def read_image_dims(self, sess, image_data):
        image = self.decode_jpeg(sess, image_data)
        return image.shape[0], image.shape[1]

    def decode_jpeg(self, sess, image_data):
        image = sess.run(self._decode_jpeg,
                         feed_dict={self._decode_jpeg_data: image_data})
        assert len(image.shape) == 3
        assert image.shape[2] == 3
        return image


def _get_filenames_and_classes(dataset_dir):
    # flower_root = os.path.join(dataset_dir, 'flower_photos')
    directories = []
    class_names = []
    for filename in os.listdir(dataset_dir):
        path = os.path.join(dataset_dir, filename)
        if os.path.isdir(path):
            directories.append(path)
            class_names.append(filename)

    photo_filenames = []
    for directory in directories:
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            photo_filenames.append(path)

    return photo_filenames, sorted(class_names)


def _get_dataset_filename(file_pre_fix, dataset_dir, shard_id):
    output_filename = '%s_%05d-of-%05d.tfrecord' % (file_pre_fix, shard_id, _NUM_SHARDS)
    return os.path.join(dataset_dir, output_filename)


def _convert_dataset(filenames, class_names_to_ids, output_dir):
    num_per_shard = int(math.ceil(len(filenames) / float(_NUM_SHARDS)))
    with tf.Graph().as_default():
        image_reader = ImageReader()
        with tf.Session('') as sess:
            for shard_id in range(_NUM_SHARDS):

                file_data_dir_name = filenames[0].split('/')[3]
                if file_data_dir_name == 'test_sample':
                    file_pre_fix = 'flowers_validation'
                elif file_data_dir_name == 'train_sample':
                    file_pre_fix = 'flowers_train'

                output_filename = _get_dataset_filename(
                    file_pre_fix, output_dir, shard_id)
                with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
                    start_ndx = shard_id * num_per_shard
                    end_ndx = min((shard_id + 1) * num_per_shard, len(filenames))
                    for i in range(start_ndx, end_ndx):
                        try:
                            sys.stdout.write('\r>> Converting image %d/%d shard %d' % (
                                i + 1, len(filenames), shard_id))
                            sys.stdout.flush()

                            # Read the filename:
                            image_data = tf.gfile.FastGFile(filenames[i], 'rb').read()
                            height, width = image_reader.read_image_dims(sess, image_data)
                            class_name = os.path.basename(os.path.dirname(filenames[i]))
                            class_id = class_names_to_ids[class_name]
                            example = image_to_tfexample(
                                image_data, b'jpg', height, width, class_id)
                            tfrecord_writer.write(example.SerializeToString())
                        except:
                            sys.stderr.write('ERROR IMAGE id`{}` path`{}`\n'.format(i + 1, filenames[i]))
                            continue

    sys.stdout.write('\n')
    sys.stdout.flush()


def _dataset_exists(dataset_dir):
    for shard_id in range(_NUM_SHARDS):
        output_filename = _get_dataset_filename(
            dataset_dir, shard_id)
        if not tf.gfile.Exists(output_filename):
            return False
    return True


def run():
    path = args()
    train_sample_dir = path['train_sample_dir']
    valid_sample_dir = path['valid_sample_dir']
    test_sample_dir = path['test_sample_dir']
    for i in [train_sample_dir, valid_sample_dir, test_sample_dir]:
        input_dir = i
        output_dir = i

        if not tf.gfile.Exists(output_dir):
            tf.gfile.MakeDirs(output_dir)

        # if _dataset_exists(output_dir):
        #     print('Dataset files already exist. Exiting without re-creating them.')
        #     return

        photo_filenames, class_names = _get_filenames_and_classes(input_dir)
        class_names_to_ids = dict(zip(class_names, range(len(class_names))))

        random.seed(_RANDOM_SEED)
        random.shuffle(photo_filenames)

        _convert_dataset(photo_filenames, class_names_to_ids,
                         output_dir)

        labels_to_class_names = dict(zip(range(len(class_names)), class_names))
        write_label_file(labels_to_class_names, output_dir)

        print('\nFinished converting the {} dataset!\n'.format(i))


# if __name__ == '__main__':
#     run()


if __name__ == '__main__':
    input_dataset_dir = 'data/flowers/flower_photos'
    output_dataset_dir = 'data/flowers/output'
    tfrecord_output_dir = 'data/flowers/tfrecord'
    output_dir = tfrecord_output_dir

    data_set_classification(input_dataset_dir, output_dataset_dir)


    train_sample_dir = os.path.join(output_dataset_dir, 'train_sample')
    valid_sample_dir = os.path.join(output_dataset_dir, 'valid_sample')
    test_sample_dir = os.path.join(output_dataset_dir, 'test_sample')
    # for i in [train_sample_dir, valid_sample_dir, test_sample_dir]:
    for i in [train_sample_dir, test_sample_dir]:
        input_dir = i
        # output_dir = i

        if not tf.gfile.Exists(output_dir):
            tf.gfile.MakeDirs(output_dir)

        # if _dataset_exists(output_dir):
        #     print('Dataset files already exist. Exiting without re-creating them.')
        #     return

        photo_filenames, class_names = _get_filenames_and_classes(input_dir)
        class_names_to_ids = dict(zip(class_names, range(len(class_names))))

        random.seed(_RANDOM_SEED)
        random.shuffle(photo_filenames)

        _convert_dataset(photo_filenames, class_names_to_ids,
                         output_dir)

        labels_to_class_names = dict(zip(range(len(class_names)), class_names))
        write_label_file(labels_to_class_names, output_dir)

        print('\nFinished converting the {} dataset!\n'.format(i))
