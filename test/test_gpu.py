# -*- coding: utf-8 -*-
"""
   File Name：     test_gpu.py
   Description :  test gpu environment for tensorflow and pytorch, like gpu driver/cuda/cudnn.
   Author :       yuanfang
   date：         2020/08/06
"""

import tensorflow as tf
#print('gpu_device_name=',tf.test.gpu_device_name())
a = tf.test.is_built_with_cuda()
b = tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)
print(a)
print(b)
# sess =tf.Session(config=tf.ConfigProto(log_device_placement=True))
print("Testing tensorflow gpu is done, then go to the pythorch's ")





import torch
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))
print(torch.cuda.is_available())
print("Testing pytorch gpu section is done")
