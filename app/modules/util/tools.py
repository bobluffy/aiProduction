# -*- coding: utf-8 -*-
"""
   File Name：     tools.py
   Description :  tools for supporting the inner functions
   Author :       yuanfang
   date：         2020/08/06
"""

import hashlib
import time
from functools import wraps
import pandas as pd

from app.modules.util.logger_helper import ServerLogger

logger = ServerLogger("SmartTagger.").get_logger()


def func_timer(function):
    """
    timer
    :param function: counting time consumption
    :return: None
    """

    @wraps(function)
    def function_timer(*args, **kwargs):
        # logger.info('[Function: {name} start...]'.format(name=function.__name__))
        print('[Function: {name} start...]'.format(name=function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        # logger.info('[Function: {name} finished, spent time: {time:.6f}s]'.format(name=function.__name__, time=t1 - t0))
        logger.debug('[Function: {name} finished, spent time: {time:.6f}s]'.format(name=function.__name__, time=t1 - t0))
        return result

    return function_timer


