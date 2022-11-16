# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   cmd_tools
# FileName:     cli.py
# Author:      Jakiro
# Datetime:    2022/5/25 16:37
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

from cli.excel_tools import ExcelHandle
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='DataTools')
    # 声明命令行可用参数
    parser.add_argument('--type', choices=['excel', 'yaml', 'dict', 'txt'], default='excel', type=str,
                        help='--type  {excel,yaml,dict,txt} : 指定操作文件的类型')
    parser.add_argument('--path', type=str, help='--path 旧文件名：指定旧文件目录')
    parser.add_argument('--index', type=int, help='--index 列号:操作前几列数据')
    parser.add_argument('-sc', action='store_true', help='-sc :统计有多少页数据')
    parser.add_argument('-ad', action='store_true', help='-ad :打印所有的数据')
    parser.add_argument('-ca', action='store_true', help='-ca :统计每页有多少行数据')
    parser.add_argument('-si', action='store_true', help='-si :打印sheet名与下标索引')
    parser.add_argument('--nf', type=str, help='--nf new_file_name : 生成文件文件名')
    parser.add_argument('--fi', type=str, nargs=2,
                        help='--if int:列号 field1,field2 : 筛选当前列号下 属于{field1,filed2}的数据 并保存到新文件中 必须有--nf参数')
    parser.add_argument('--cs', type=str,
                        help='--cs sheet_index1,sheet_index2 : 筛选下标索引 属于{sheet_index1,sheet_index2}的数据 并保存到新文件中 必须有--nf参数')
    parser.add_argument('-v', action='store_true', help='-v : 打印版本信息')
    parser.add_argument('-cas', action='store_true', help='将统计的信息保存在新文件夹中,此选项--path 与--nf 必填')

    # 获得命令行参数
    args = parser.parse_args()
    print('命令行接收参数', args)
    # print('当前工作目录：', os.listdir)
    type_option = args.type
    base_data_path = f'data/{type_option}/'

    # 根据执行操作类型判断目录是否存在
    if not os.path.exists(base_data_path):
        os.mkdir(base_data_path)
        print(f'mk {type_option} directory')

    # 判断源文件是否存在
    old_file_path = f"data/old/" + args.path
    if not os.path.exists(old_file_path):
        print(f'{old_file_path}old_file_path not exist')

    excel_index = args.index
    # 打印版本信息
    if args.v:
        print('DataTools v1.0.1')

    # 需要创建文件的目录存在判断
    if args.nf:
        new_file_path = base_data_path + args.nf
        if os.path.exists(new_file_path):
            raise ValueError('new file path is exists')
        print(f'create new file {new_file_path}')

    if type_option == 'excel':
        if not old_file_path.endswith('.xlsx'):
            print('error: file format is not excel')

        # 初始化excel handle
        if excel_index:
            eh = ExcelHandle(file_path=old_file_path, index=excel_index)
        else:
            eh = ExcelHandle(file_path=old_file_path)

        # 打印页统计
        if args.sc:
            print('页统计', eh.sheet_count)

        # 打印所有数据
        if args.ad:
            print('所有数据：', eh.all_data)

        # 按分页打印所有统计
        if args.ca:
            print('按分页打印所有统计', eh.count_all_sheet)

        # 按分页打印所有统计
        if args.si:
            print('按分页打印所有统计', eh.sheet_index)

        # 按条件筛选用例
        if args.fi and not args.cs:
            print('processing 按条件筛选用例')
            if new_file_path:
                eh.copy_excel_all_data(new_file_path, int(args.fi[0]), args.fi[1].split(','))
            else:
                print('error: need nf')

        # 按条件复制sheet页
        if args.cs and not args.fi:
            print('processing 按条件复制sheet页')
            if new_file_path:
                eh.copy_sheet(new_file_path, args.cs.split(','))
            else:
                print('error: need nf')

        if args.cs and args.fi:
            print('processing 按条件筛选复制指定sheet页')
            if new_file_path:
                file_path = eh.copy_sheet(new_file_path, args.cs.split(','))
                eh = ExcelHandle(file_path=file_path)
                print(args.fi)
                eh.copy_excel_all_data(new_file_path,int(args.fi[0]), args.fi[1].split(','))
            else:
                print('error: need nf')

        # 统计所有sheet页中的行数
        if args.cas:
            print('processing 按条件复制sheet页并保存到新文件中')
            if new_file_path:
                eh.count_all_sheet_write(new_file_path)
            else:
                print('error: need nf')
