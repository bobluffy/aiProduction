# -*- coding: utf-8 -*-
"""
   File Name：     error.py
   Description :  customized exception
   Author :       yuanfang
   date：         2020/08/06
"""

class Addr_St_Error(RuntimeError):
    """
    自定义异常
    """

    def __init__(self, status_code: str, error_info: str, message: str, *args: object) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.error_info = error_info
        self.message = message

    def __str__(self) -> str:
        return str(self.message)
