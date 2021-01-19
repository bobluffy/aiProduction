# -*- coding: utf-8 -*-
"""
   File Name：     main.py
   Description :  the main logic of address finding service
   Author :       yuanfang
   date：         2020/12/15
"""

from app.modules.util.error import Addr_St_Error
from app.modules.util.tools import logger, func_timer
from app.inner_confs.constants_config import ResponseCode


class AIFlow:
    def __init__(self):
        self.__matcher__ = Matcher()
        logger.debug(f"preloading labels'da words={self.__matcher__.get_words()}")
        logger.debug(f"preloading labels = {self.__matcher__.get_lables()}")

    def check_input(self, data):
        logger.debug("check_param start")
        body_data = data

        if not isinstance(body_data, dict) or "instances" not in body_data:
            raise Addr_St_Error(ResponseCode.TEXT_TAGER_PARAM_ERROR_CODE,
                                ResponseCode.TEXT_TAGER_PARAM_ERROR_INFO, 'instances格式错误，应该是dic')

        if "keywords" in body_data:
            if not isinstance(body_data['keywords'], dict):
                raise Addr_St_Error(ResponseCode.TEXT_TAGER_PARAM_ERROR_CODE,
                                    ResponseCode.TEXT_TAGER_PARAM_ERROR_INFO, 'keywords格式错误，应该是dic')

        if "descriptions" in body_data:
            if not isinstance(body_data['descriptions'], dict):
                raise Addr_St_Error(ResponseCode.TEXT_TAGER_PARAM_ERROR_CODE,
                                    ResponseCode.TEXT_TAGER_PARAM_ERROR_INFO, 'keywords格式错误，应该是dic')

        for em in body_data['instances']:
            if not isinstance(em, dict):
                raise Addr_St_Error(ResponseCode.TEXT_TAGER_PARAM_ERROR_CODE,
                                    ResponseCode.TEXT_TAGER_PARAM_ERROR_INFO, 'instances格式错误，应该是dic')
            if 'id' not in em:
                raise Addr_St_Error(ResponseCode.TEXT_TAGER_PARAM_ERROR_CODE,
                                    ResponseCode.TEXT_TAGER_PARAM_ERROR_INFO, 'instances格式错误，元素缺失id')
            if 'text' not in em:
                raise Addr_St_Error(ResponseCode.TEXT_TAGER_PARAM_ERROR_CODE,
                                    ResponseCode.TEXT_TAGER_PARAM_ERROR_INFO, 'instances格式错误，元素缺失text')

    def check_output(self, data):
        '''
        check the output result
        :param data: the query info
        :return: the final result
        '''
        pass

    @func_timer
    def main_flow(self, data, demo=False):
        pass

    @func_timer
    def process(self, text, words_like=[], descriptions=[]):
        '''
        the whole process of the address finding process
        :param text: the query data
        :return: the found addresses
        '''
        pass
