"""
AlexNet 模型的实际测试。

@author: wgshun
"""

import tensorflow.compat.v1 as tf
from Do_Ident.img_classification.tf_alexnet import AlexNet
import sys, os

import time
import sqlite3

# val_file = 'data/试纸5/牛/60-5.png'
# val_file = sys.argv[1]
# result_file = sys.argv[2]
# num_classes = 10

# IMAGENET_MEAN = tf.constant([123.68, 116.779, 103.939], dtype=tf.float32)
#
# conn = sqlite3.connect('test1.db')
# c = conn.cursor()

tf.disable_eager_execution()

def parse_function_val(filename):
    """Input parser for samples of the validation/test set."""
    IMAGENET_MEAN = tf.constant([123.68, 116.779, 103.939], dtype=tf.float32)
    # load and preprocess the image
    img_string = tf.read_file(filename)
    img_decoded = tf.image.decode_png(img_string, channels=3)
    img_resized = tf.image.resize_images(img_decoded, [227, 227])
    # img_resized = tf.image.resize_image_with_crop_or_pad(img_decoded, 227, 227)
    # img_resized = tf.cast(img_resized, tf.float32)
    img_centered = tf.subtract(img_resized, IMAGENET_MEAN)

    # RGB -> BGR
    img_bgr = img_centered[:, :, ::-1]

    return img_bgr
# Place data loading and preprocessing on the cpu
def predict(val_file, num_classes=10):
    with tf.device('/cpu:0'):

        # TF placeholder for graph input and output
        x = tf.placeholder(tf.float32, [None, 227, 227, 3])
        keep_prob = tf.placeholder(tf.float32)

        # Initialize model
        model = AlexNet(x, keep_prob, num_classes, [], weights_path='..\TestPaper\Do_Ident\img_classification\model\checkpoints\model_epoch196.ckpt')

        # Link variable to model output
        score = model.fc8

        # Start Tensorflow session
        with tf.Session() as sess:

            # Initialize all variables
            sess.run(tf.global_variables_initializer())

            # Load the pretrained weights into the non-trainable layer
            model.load_model(sess)

            # Validate the model on the entire validation set
            #print("Start validation")
            # t0 = time.time()
            val_data = parse_function_val(val_file, )
            input = val_data.eval().reshape([1, 227, 227, 3])
            sco = sess.run(score, feed_dict={x: input, keep_prob: 1.})
            # if tf.argmax(sco, 1).eval()[0] > 3:
            #     result = str(tf.argmax(sco, 1).eval())+'超标'
            # else:
            #     result = '合格'
           # print(time.time()-t0)

            # cursor = c.execute('''UPDATE mnnu_in_testpaper SET result={result}} WHERE paper_idx={id}};'''.format(id=val_file.split('\\')[-1].strip('.jpg'), result=str(tf.argmax(sco, 1).eval())))
            rut = tf.argmax(sco, 1).eval()[0]
            if rut>3:
                return '['+str(rut)+']'+"  超标"
            else:
                return '['+str(rut)+']'+"  正常"
            # return str(tf.argmax(sco, 1).eval()[0])
            # if os.path.exists(result_file):
            #     os.remove(result_file)
            # with open(result_file, 'w+') as result_fp:
            #     # result_fp.write(str(tf.argmax(sco, 1).eval()))
            #     result_fp.writelines(result)
