#-*-coding:utf-8-*-

import tensorflow as tf 

with tf.Session() as sess:
    filename = ['A.jpg', 'B.jpg', 'C.jpg']
    # string_input_producer会产生一个文件名队列
    filename_queue = tf.train.string_input_producer(filename, shuffle=False, num_epochs=5)
    # reader从文件名队列中读数据。对应的方法是reader.read
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    # tf.train.string_input_producer定义了一个epoch变量，要对它进行初始化
    tf.local_variables_initializer().run()
    # 使用start_queue_runners之后，才会开始填充队列
    threads = tf.train.start_queue_runners(sess=sess)
    i = 0
    while(i<15):
        i += 1
        # 获取图片数据并保存
        image_data = sess.run(value)
        with open('result/test_%d.jpg' % i, 'wb') as f:
            f.write(image_data)