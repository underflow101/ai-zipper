'''
quantization/utils.py
Dev. underflow101

Contains utilities for quantization
'''

from __future__ import absolute_import, division, print_function
import tensorflow as tf
import cv2
import numpy as np
import glob, os

def load_h5(model_path):
  print("Loading .h5 keras model file...")
  model = tf.keras.models.load_model(model_path)
  optimizer = tf.keras.optimizers.SGD()
  model.compile(optimizer=optimizer,
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
  
  return model

def _rep_data_gen(type='', im_path='', img_size=224, batch_size=1):
    img_arr = []
    for item in im_path:
        file_name = item
        img = cv2.imread(file_name)
        img = cv2.resize(img, (img_size, img_size))
        img = img / 255.0
        if type == 'U8':
            img = img.astype(np.uint8)
        elif type == 'INT8':
            img = img.astype(np.int8)
        img_arr.append(img)
    img_arr = np.array(img_arr)
    img = tf.data.Dataset.from_tensor_slices(img_arr).batch(batch_size)
    for i in img.take(batch_size):
        yield [i]