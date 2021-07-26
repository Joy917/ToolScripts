#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2021/07/26 23:30
# @Author  : Joy
# @Version : python3.9
# @Desc    : Google 机翻


import os
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def translate(text, target_language="zh-CN"):
    """
    机翻入口方法，多次翻译避免网络问题
    :param text: 待翻译内容
    :param target_language: 目标语言
    :return: 翻译结果
    """
    driver = get_webdriver()
    result = ""
    for i in range(2):
        result = translate_with_webdriver(text, driver, target_language=target_language)
        if result.strip() != "":
            break
    driver.quit()
    if result.strip() == "":
        result = translate_with_api(text)
    return result


def translate_with_api(text, target_language="zh-CN"):
    """
    请求谷歌翻译接口，次数过多会被限制访问，大概在20次左右
    :param text: 待翻译内容
    :param target_language: 目标语言
    :return: 翻译结果
    """
    result = ""
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "yourCookie"
    }
    if text and isinstance(text, str) and text.strip() != "":
        url = "https://translate.google.com/translate_a/single?"
        params = {"client": "gtx", "sl": "auto", "tl": target_language, "dt": "t", "ie": "UTF-8", "oe": "UTF-8",
                  "q": text}
        try:
            r = requests.get(url + urlencode(params), headers=header)
            if r.status_code == 200:
                # 拼接语义断句的各部分
                for item in r.json()[0]:
                    result += item[0]
        except:
            pass
    return result


def translate_with_webdriver(text, driver, target_language="zh-CN"):
    """
    模拟浏览器翻译
    :param text: 待翻译内容
    :param driver: 浏览器驱动
    :param target_language: 目标语言
    :return: 翻译结果
    """
    result = ""
    if text and isinstance(text, str) and text.strip() != "":
        # 超过5000字符需要多次翻译
        # TODO：非自然语义断句需处理
        if len(text) > 5000:
            count = len(text) // 5000 + 1
            temp_result = ""
            for i in range(0, count):
                temp_text = text[5000 * i:5000 * (i + 1)]
                temp_result += translate_with_webdriver(temp_text, driver, target_language)
            return temp_result
        url = f"https://translate.google.cn/?"
        params = {"sl": "auto", "tl": target_language, "op": "translate", "text": text}
        try:
            driver.get(url + urlencode(params))
            element = driver.find_element_by_xpath(
                "//div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div[1]/div[1]/span[1]/span[1]")
            soup = BeautifulSoup(element.get_attribute('innerHTML'), "html.parser")
            result = soup.find_all("span")[0].string
        except Exception as exc:
            pass
    return result


def get_webdriver():
    # 模拟浏览器登录
    options = webdriver.ChromeOptions()
    # 加速：关闭可视化
    options.add_argument('--headless')
    # 加速：关闭图片视频加载
    options.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    return driver


def project_dir():
    # D:\projects\ToolScripts
    return os.path.abspath(os.path.dirname(__file__))


# chrome 浏览器驱动路径
DRIVER_PATH = os.path.join(project_dir(), "chromedriver.exe")

# 支持语言缩写对照表
SUPPORT_LANGUAGE = {'afrikaans': 'af',
                    'arabic': 'ar',
                    'belarusian': 'be',
                    'bulgarian': 'bg',
                    'catalan': 'ca',
                    'czech': 'cs',
                    'welsh': 'cy',
                    'danish': 'da',
                    'german': 'de',
                    'greek': 'el',
                    'english': 'en',
                    'esperanto': 'eo',
                    'spanish': 'es',
                    'estonian': 'et',
                    'persian': 'fa',
                    'finnish': 'fi',
                    'french': 'fr',
                    'irish': 'ga',
                    'galician': 'gl',
                    'hindi': 'hi',
                    'croatian': 'hr',
                    'hungarian': 'hu',
                    'indonesian': 'id',
                    'icelandic': 'is',
                    'italian': 'it',
                    'hebrew': 'iw',
                    'japanese': 'ja',
                    'korean': 'ko',
                    'latin': 'la',
                    'lithuanian': 'lt',
                    'latvian': 'lv',
                    'macedonian': 'mk',
                    'malay': 'ms',
                    'maltese': 'mt',
                    'dutch': 'nl',
                    'norwegian': 'no',
                    'polish': 'pl',
                    'portuguese': 'pt',
                    'romanian': 'ro',
                    'russian': 'ru',
                    'slovak': 'sk',
                    'slovenian': 'sl',
                    'albanian': 'sq',
                    'serbian': 'sr',
                    'swedish': 'sv',
                    'swahili': 'sw',
                    'thai': 'th',
                    'filipino': 'tl',
                    'turkish': 'tr',
                    'ukrainian': 'uk',
                    'vietnamese': 'vi',
                    'yiddish': 'yi',
                    'chinese_simplified': 'zh-CN',
                    'chinese_traditional': 'zh-TW',
                    'auto': 'auto'}
