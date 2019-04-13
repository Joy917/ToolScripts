#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/10 23:19
# @Author: Joy
# @IDE  : PyCharm

import os
import re
import sys

from common.utils import common_error
from common.utils import change_file_enc


def exchange_captions_to_plays(captions_dir: str, des_dir=None):
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
						content_search = re.search(content_parttern, line)
						if content_search:
							fw.write("{}".format(content_search.group(2)))
							fw.write("{}\n\n".format(content_search.group(1)))
		except:
			common_error("exchange {} error".format(file_path))
		else:
			print("{} was exchanged success ! ".format(file_name))


if __name__ == '__main__':
	content_parttern = re.compile(
		r"0,0,0,,(.+)\\N\{\\fs14\}([\w\s\"\'\-.\,\?\!\$]+)|0,0,0,,(.+)\{\\fs14\}\\N([\w\s\"\'\-.\,\?\!\$]+)")
	captions_dir = "H:\Codes\Git-Projects\ToolScripts\Superstore\captions\S01"
	des_dir = "H:\Codes\Git-Projects\ToolScripts\Superstore\plays"
	# change_file_enc(captions_dir)
	exchange_captions_to_plays(captions_dir, des_dir)
