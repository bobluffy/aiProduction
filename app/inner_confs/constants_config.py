# -*- coding: utf-8 -*-
"""
   File Name：     constants_config.py
   Description :  ResponseCode
   Author :       yuanfang
   date：         2020/08/06
"""



class ResponseCode(object):
    """
    server's response status code and its description
    """

    # 响应成功标识
    TEXT_TAGER_SUCCESS = '1'
    # 响应失败标识
    TEXT_TAGER_FAIL = '0'

    # 成功状态码
    TEXT_TAGER_SUCCESS_CODE = '000000'
    TEXT_TAGER_SUCCESS_INFO = '成功'

    # 通用业务码前缀
    TEXT_TAGER_COMMON_STATUS_CODE = '01'
    # 通用错误码前缀
    TEXT_TAGER_COMMON_ERROR_CODE = '10'

    # 内部异常
    TEXT_TAGER_SYSTEM_ERROR_CODE = TEXT_TAGER_COMMON_ERROR_CODE + '0001'
    TEXT_TAGER_SYSTEM_ERROR_INFO = '系统服务繁忙，请稍候再试'

    # 参数错误
    TEXT_TAGER_PARAM_ERROR_CODE = TEXT_TAGER_COMMON_ERROR_CODE + '0002'
    TEXT_TAGER_PARAM_ERROR_INFO = '参数错误'