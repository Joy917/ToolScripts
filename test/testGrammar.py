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
    N = input("请输入计算次数:\n")
    integer_list = []
    result = ""
    for i in range(int(N)):
        a = input("请输入第{}组数字,按回车结束:\n".format(i + 1))
        integer_list.append(int(a))

    for item in integer_list:
        count = 0
        for i in range(1, item + 1):
            i = str(i)
            count += i.count("6")
        result += str(count) + "\n"
    print(result)


def ProC(s: str):
    result = ""
    for ss in s.split("\n"):
        num = (ss.split())
        X = int(num[0])
        Y = int(num[1])
        Z = int(num[2])
        if X == 1 or Y == 1:
            result += "YE5\n"
        else:
            if X > Y:
                n = X // Y
                if X - Y * n == 1:
                    result += "YE5\n"
                else:
                    result += "N0\n"
            else:
                n = Y // X
                if Y - X * n == 1:
                    result += "YE5\n"
                else:
                    result += "N0\n"
    return result.rstrip("\n")

if __name__ == "__main__":
    print(ProC("1 2 4\n"
         "2 8 13\n"
         "2 7 13"))

