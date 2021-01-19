# -*- coding: utf-8 -*-
"""
   File Name：     path_config.py
   Description :  configs of code-base varaibles
   Author :       yuanfang
   date：         2020/08/19
"""
import os

# 1. parameters config
host_hdfs = '10.XXXXX'
port_hdfs = '9870'

# 2. path config:
print(os.pardir)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
project_root = project_root.replace('\\', '/')
app_dir = project_root + '/app/'
outer_confs_dir = project_root + '/confs/'
