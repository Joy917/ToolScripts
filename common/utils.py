#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/11 23:06
# @Author: Joy
# @IDE  : PyCharm

import os
import io
import sys
from chardet.universaldetector import UniversalDetector


def common_error(data: str):
    """
    捕获异常时打印详细错误信息，用于 except 后
    :param data:
    :return:
    """
    info = sys.exc_info()
    print("{}:".format(data), str(info[0]), ",", str(info[1]))


def pprint(*args):
    """
    高亮打印，多个入参时结果以空格分隔
    :param args:
    :return:
    """
    args_list = []
    if args:
        for arg in args:
            args_list.append(str(arg))
    data = " ".join(args_list)
    print("\033[7;34;40m{}\033[4m".format(data), end="")  # 高亮蓝底白字
    # print("\033[1;34m{}\033[4m".format(data), end="")  # 加粗黑底蓝字


def get_file_enc(filepath: str) -> str:
    """
    获取文件编码
    :param filepath:
    :return:
    """
    with open(filepath, 'rb') as frb:
        detector = UniversalDetector()
        for line in frb.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result["encoding"]


def change_file_enc(files_dir: str, output_encoding="utf-8"):
    """
    转换给定及子孙目录下所有文件的编码格式，默认utf-8
    :param files_dir:
    :param output_encoding:
    :return:
    """
    files_list = []
    try:
        for root, dirs, files in os.walk(files_dir, topdown=False):
            for name in files:
                files_list.append(os.path.join(root, name))
    except:
        common_error("get files error")

    try:
        for filename in files_list:
            file_encoding = get_file_enc(filename)
            with io.open(filename, encoding=file_encoding) as f:
                text = f.read()
            with io.open(filename, 'w', encoding=output_encoding) as f:
                f.write(text)
    except:
        common_error("change file enc error")


if __name__ == "__main__":
    # just for the test
    # dir_path = "H:\Codes\Git-Projects\ToolScripts\Superstore\captions\S01"
    pprint("123", 333)
