'''
quantization/quant.py
Dev. underflow101

- Supports tflite quantization process
    - Float32 Quantization
    - Float16 Quantization
    - INT8 Quantization
    - UINT8 Quantization

@function: quantization(model=None, dtype='float32', repre='', img_size=None)
@param:
    - model: default=None
        - Select either model class object, SavedModel, or keras .h5 model file path
        - Supports Sequential/Functional/Subclassed models
    - dtype: default='float32'
        - Select quantization target option (String format)
        - Supports target type of following:
            - 'float32'
            - 'float16'
            - 'int8'
            - 'uint8'
    - repre: default=''
        - Directory path for representative datasets (String format)
        - Necessary for INT8/UINT8 Quantization, leave blank for Float32/Float16 Quantization
    - img_size: default=None
        - Image size for representative datasets (int format)
        - Necessary for INT8/UINT8 Quantization, leave blank for Float32/Float16 Quantization
        - img_size should match with input tensor/image size of the original network
'''

from __future__ import absolute_import, division, print_function
import tensorflow as tf
import cv2
import numpy as np
import glob, os

from quantization.utils import *

