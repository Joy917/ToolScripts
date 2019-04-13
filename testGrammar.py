#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/13 10:15
# @Author: Joy
# @IDE  : PyCharm

def test_input():
	N, sum_str = input(), ""
	for i in range(int(N)):
		a, b = input().split()
		sum_str += str(int(a) + int(b)) + "\n"
	print(sum_str)

if __name__ == "__main__":
	test_input()
