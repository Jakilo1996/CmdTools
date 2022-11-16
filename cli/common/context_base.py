# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   cmd_tools
# FileName:     context_base.py
# Author:      Jakiro
# Datetime:    2022/5/25 15:57
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

from functools import wraps


class ContextMangerBase():
    def __init__(self, func, args, kwargs):
        # print(args)
        self.gene = func(*args, **kwargs)

    def __enter__(self):
        # print('__enter_-')
        try:
            return next(self.gene)
        except StopIteration:
            raise RuntimeError('generation did`t yield') from None

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('__exit__')
        if exc_type == None:
            try:
                # print('__exit__try')
                next(self.gene)
            # 此处的作用是为了忽略 迭代对象 第二次next 的 StopIteration异常
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")

        else:
            try:
                self.gene.throw(exc_type, exc_val, exc_tb)
            except:
                raise
            raise RuntimeError("generator didn't stop after throw()")


def context_manager(func, ):
    '''
    params: func 被装饰的函数对象，必须是一个生成器函数，缺省参数为装饰器函数的实参
    '''

    @wraps(func)
    def inner(*args, **kwargs):
        return ContextMangerBase(func, args, kwargs)

    return inner
