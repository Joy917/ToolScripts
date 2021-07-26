#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2021/07/26 23:34
# @Author  : Joy
# @Version : python3.9
# @Desc    : 日期工具类

import datetime
import re


def format_date(input_date):
    """
    date examples:
    8 hours ago
    30 minutes ago
    3 days ago
    17 April 2017
    17 April = 17 April currentYear
    7 April = 07 April currentYear
    TODO：April 9, 2021 04:06 pm ET
    :param input_date: string
    :return: int 20170417
    """
    result = -1
    try:
        now = datetime.datetime.now()
        # 非常规日期校验
        days_match = re.match(r"(\d+)\s+day.+ago", input_date)
        if days_match:
            n_days_before = now - datetime.timedelta(days=int(days_match.group(1)))
            return n_days_before.strftime("%Y%m%d")
        hours_match = re.match(r"(\d+)\s+hour.+ago", input_date)
        if hours_match:
            n_hours_before = now - datetime.timedelta(hours=int(hours_match.group(1)))
            return n_hours_before.strftime("%Y%m%d")
        minutes_match = re.match(r"(\d+)\s+minute.+ago", input_date)
        if minutes_match:
            n_minutes_before = now - datetime.timedelta(minutes=int(minutes_match.group(1)))
            return n_minutes_before.strftime("%Y%m%d")

        date_slice = re.split(r"\s+", input_date.strip())
        day = date_slice[0]
        if len(day) == 1: day = "0" + day
        # 处理脏数据
        month = MONTH_DICT.get(date_slice[1])
        if not month: month = "01"
        year = "2021"
        if len(date_slice) == 2:
            year = now.strftime("%Y")
        elif len(date_slice) == 3:
            year = date_slice[2]
        result = int(f"{year}{month}{day}")
        return result
    except:
        return result


def now_timestamp(mode="timestamp"):
    """
    获取当前时间戳
    :param mode: 返回模式
    :return: 时间戳
    """
    result = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    if mode == "human":
        result = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    return result


MONTH_DICT = {"January": "01",
              "February": "02",
              "March": "03",
              "April": "04",
              "May": "05",
              "June": "06",
              "July": "07",
              "August": "08",
              "September": "09",
              "October": "10",
              "November": "11",
              "December": "12"}
