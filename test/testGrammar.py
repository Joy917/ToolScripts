#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/13 10:15
# @Author: Joy
# @IDE  : PyCharm
"""
Python3.7 模块及语法测试
"""


def t_input():
	"""
	input内置函数：注意点，接受字符串无法自动转换类型
	:return:
	"""
	N, sum_str = input("请输入计算次数:\n"), ""
	for i in range(int(N)):
		a, b = input("请输入第{}组数字,以空格分开,按回车结束:".format(i + 1)).split()
		sum_str += str(float(a) + float(b)) + "\n"
	print(sum_str)


if __name__ == "__main__":
	t_input()
