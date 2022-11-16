# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   cmd_tools
# FileName:     setup.py
# Author:      Jakiro
# Datetime:    2022/5/26 16:24
# Description:  打包相关文件
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import setuptools

'''
将工具打包成可执行命令
'''

setuptools.setup(
    # 项目介绍
    name='DataToolsJK',
    # 版本号
    version='1.0',
    # author
    author='Jakiro',
    url='https://github.com/Jakilo1996/CmdTools.git',
    author_email='17709005281@163.com',
    description='用例筛选工具',
    # 需要安装的第三方依赖
    install_requires=[
        'openpyxl'
    ],
    # 此项很重要，如果不自动查找依赖包，会导致运行时的找不到包错误
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    # 可执行文件的函数入口
    py_modules=['cli'],
    entry_points={
        'console_scripts': [
            # 可执行文件的名称=执行的具体代码方法
            'DataTools=cli.cli:main'
        ]
    },
    # 决定安装位置
    zip_safe=False,
    # 是否导入MANIFEST.in目录中的文件
    # include_package_data=True
)
