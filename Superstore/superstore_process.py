# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/10 23:19
# @Author  : Joy
# @Version : python3.6

import os
import re

from common.utils import common_error


def exchange_captions_to_plays(captions_dir: str, des_dir=None):
    content_parttern1 = re.compile(r"0,,([\u4E00-\u9FA5\w\s\"\'\-.\,\?\!\$]+)\\N\{\\fs14\}([\w\s\"\'\-.\,\?\!\$]+)")
    content_parttern2 = re.compile(r"0,,([\u4E00-\u9FA5\w\s\"\'\-.\,\?\!\$]+)\{\\fs14\}\\N([\w\s\"\'\-.\,\?\!\$]+)")
    if des_dir is None:
        des_dir = captions_dir
    file_list = os.listdir(captions_dir)
    for file_name in file_list:
        if not file_name.endswith(".ass"):
            continue
        file_path = os.path.join(captions_dir, file_name)
        new_filename = file_name.rsplit(".")[0] + ".txt"
        play_path = os.path.join(des_dir, new_filename)
        try:
            with open(file_path, "r", encoding="utf-8") as fr:
                with open(play_path, "w", encoding="utf-8") as fw:
                    for line in fr.readlines():
                        if line.__contains__("本字幕由") or line.__contains__("仅供学习使用"):
                            continue
                        content_search1 = re.search(content_parttern1, line)
                        content_search2 = re.search(content_parttern2, line)
                        if content_search1:
                            fw.write("{}".format(content_search1.group(2)))
                            fw.write("{}\n\n".format(content_search1.group(1)))
                        elif content_search2:
                            fw.write("{}".format(content_search2.group(2)))
                            fw.write("{}\n\n".format(content_search2.group(1)))
        except:
            common_error("exchange {} error".format(file_path))
        else:
            print("{} was exchanged success ! ".format(file_name))


if __name__ == '__main__':
    captions_dir = "H:\Codes\Git-Projects\ToolScripts\Superstore\captions\S01"
    des_dir = "H:\Codes\Git-Projects\ToolScripts\Superstore\plays"
    # change_file_enc(captions_dir)
    exchange_captions_to_plays(captions_dir, des_dir)
