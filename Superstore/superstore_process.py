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


def exchange_captions_to_plays(captions_dir: object) -> object:
	file_list = os.listdir(captions_dir)
	for file_name in file_list:
		file_path = os.path.join(captions_dir, file_name)
		try:
			with open(file_path, "r", encoding="utf-8") as frb:
				for line in frb.readlines():
					# print(line)
					pass
		except:
			common_error("exchange {} error".format(file_path))
		else:
			print("{} was exchanged success ! ".format(file_name))


if __name__ == '__main__':
	content_parttern = re.compile("")
	captions_dir = "H:\Codes\Git-Projects\ToolScripts\Superstore\captions\S01"
	change_file_enc(captions_dir)
	exchange_captions_to_plays(captions_dir)
