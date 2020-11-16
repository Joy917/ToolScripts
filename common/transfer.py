#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2020/11/16 20:33
# @Author: Joy
# @IDE  : PyCharm


import os, re


def normal_path(*args):
    return os.path.normpath(os.path.join(*args))


class Transfer:
    def __init__(self):
        self.DESKTOP_PATH = normal_path("C:/Users", os.getenv("USERNAME"), "Desktop")
        self.DEFAULT_SIZE_PER = 1024 * 1024 * 10

    def split_file(self, src_file: str, output_dir=""):
        """
        拆分文件
        :param src_file: 源文件路径
        :param output_dir: 切分文件输出目录
        :return:
        """
        if not os.path.isfile(src_file):
            raise Exception(f"The given path:{src_file} is not file!")
        if not output_dir:
            output_dir = self.DESKTOP_PATH

        file_size = os.path.getsize(src_file)
        print(f"src file size:{file_size // (1024 * 1024)} M")
        count = file_size // self.DEFAULT_SIZE_PER
        mod = file_size % self.DEFAULT_SIZE_PER
        if mod > 0: count += 1
        with open(file=src_file, mode="rb") as fr:
            # 切割源文件至目标大小
            for i in range(0, count):
                target_file = normal_path(output_dir, f"{os.path.basename(src_file)}_{i}")
                with open(file=target_file, mode="wb") as fw:
                    fw.write(fr.read(self.DEFAULT_SIZE_PER))
                    print("sub file name:", target_file)
            print("split finished!")

    def fit_file(self, files_dir: str, target_file_name: str, output_dir=""):
        """合并文件
        :param files_dir: 切分文件所在目录
        :param target_file_name: 合并文件名
        :param output_dir: 合并文件输出目录
        :return:
        """
        if not (os.path.exists(files_dir) and os.path.isdir(files_dir)):
            raise Exception(f"The given path:{files_dir} does not exist or is not a folder!")
        if not output_dir:
            output_dir = self.DESKTOP_PATH
        target_file_path = normal_path(output_dir, target_file_name)
        if os.path.exists(target_file_path):
            raise Exception("The output folder already exists target file!")
        regex = re.compile(target_file_name + "_\d+")
        split_files = []
        # 获取目标文件列表并根据编号排序
        for file in os.listdir(files_dir):
            if not re.match(regex, file):
                continue
            index = file.rsplit("_", 1)[1]
            split_files.insert(int(index), normal_path(files_dir, file))
        # 组装文件
        with open(file=target_file_path, mode="ab") as fw:
            for sub_file in split_files:
                with open(file=sub_file, mode="rb") as fr:
                    fw.write(fr.read())

        print(f"{target_file_name} fit finished!")


if __name__ == '__main__':
    file = "Hadoop权威指南_第四版_中文版.pdf"
    transfer = Transfer()
    # transfer.split_file("E:/天天向上/Hadoop权威指南_第四版_中文版.pdf")
    transfer.fit_file("C:/Users/Joy/Desktop/", file)
