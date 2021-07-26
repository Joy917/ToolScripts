#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2021/07/27 0:15
# @Author  : Joy
# @Version : python3.9
# @Desc    : Excel表格处理，只支持 .xlsx 结尾文件


import os

import openpyxl


def create_xlsx_with_head(file_path, sheet_name, head_values=None):
    """
    创建空Excel表格
    :param file_path: 指定文件路径
    :param sheet_name: sheet名
    :param head_values: 头列表
    :return:
    """
    if head_values is None:
        head_values = ["Title", "Title-CN", "Date", "URL", "Text", "Text-CN"]
    if file_path.endswith(".xlsx"):
        dir_name = os.path.dirname(file_path)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        # 新建文件和表格
        wb = openpyxl.Workbook()
        # 删除默认生成的sheet
        wb.remove(wb["Sheet"])
        sheet = wb.create_sheet(sheet_name, index=1)
        # 调整列宽
        sheet.column_dimensions['A'].width = 20.0
        sheet.column_dimensions['B'].width = 20.0
        sheet.column_dimensions['E'].width = 20.0
        sheet.column_dimensions['F'].width = 20.0
        # 添加表头
        if head_values: sheet.append(head_values)
        wb.save(file_path)  # 保存文件，注意以xlsx为文件扩展名
    else:
        print("file path must end with .xlsx")


def write_xlsx_apend(file_path, values):
    """
    向表格中增加行
    :param file_path: 文件路径
    :param values: 对象
    :return:
    """
    if os.path.isfile(file_path) and file_path.endswith(".xlsx"):
        wb = openpyxl.load_workbook(file_path)
        # 获取workbook中第一个表格
        sheet = wb[wb.sheetnames[0]]
        for value in values:
            # TODO：需修改成对象属性或者其他
            row = [value.title, value.title_cn, value.date, value.url, value.text, value.text_cn]
            sheet.append(row)
        wb.save(file_path)  # 保存文件，注意以xlsx为文件扩展名
    else:
        print("file path must end with .xlsx")
