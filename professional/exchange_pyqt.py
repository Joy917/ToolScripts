#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/02/22 23:09
# @Author: Joy
# @IDE  : PyCharm


import os

# 此处的path为UI文件存放的路径
path = r'D:\SVNzhangy\fast-transfer\src'

# 记录转换成功的文件数量
count = 0
for root, dirs, files in os.walk(path):
    filename = []
    for file in files:
        if file.endswith('.py'):
            filename2 = file.split('.')[0]
            filename.append(filename2)

    version = input("请输入1 or 2 确认pyqt转换版本(1 - pyqt4,2 - pyqt5):")

    for file in files:
        if file.endswith('.ui'):
            filename1 = file.split('.')[0]
            filename4 = filename1 + "_qt4"
            filename5 = filename1 + "_qt5"
            try:
                if "1" == str(version):
                    if filename.count(filename4) == 0:
                        os.system('pyuic4 -o %s.py %s.ui -d' % (path + '\\' + filename4, path + '\\' + filename1))
                        count += 1
                if "2" == str(version):
                    if filename.count(filename5) == 0:
                        os.system('pyuic5 -o %s.py %s.ui -d' % (path + '\\' + filename5, path + '\\' + filename1))
                        count += 1
            except Exception as e:
                print("文件转化错误，请检查是否正确安装指令对应PyQt")
                raise e

    if count == 0:
        print("暂无需要转换的UI文件")
    else:
        print('转换完毕，请查收！本次共转换 ' + str(count) + ' 个文件')
