# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   cmd_tools
# FileName:     decorator_base.py
# Author:      Jakiro
# Datetime:    2022/5/25 13:24
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import time
from functools import wraps


def timeit(prefix=None, display=True):
    '''
    我们在 timeit 中定义了 2 个内部方法，然后让 timeit 可以接收参数，返回 decorator 对象，而在 decorator 方法中再返回 wrapper 对象。
    通过这种方式，带参数的装饰器由 2 个内部方法嵌套就可以实现了。
    :param prefix:
    :return:
    '''

    def dec(func):
        @wraps(func)
        # 使用@wraps装饰器  保留 func自身的属性
        def inner(*args, **kwargs):
            start_time = time.time()
            reason = func(*args, **kwargs)
            end_time = time.time()
            if display:
                print(f'{prefix}_{func.__name__} duration {end_time - start_time}')
            return reason

        return inner

    return dec
