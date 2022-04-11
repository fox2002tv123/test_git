'''
Author: bob
Date: 2022-04-11 12:50:37
LastEditors: bob
LastEditTime: 2022-04-11 13:00:03
FilePath: \test_git\test_ocr.py
Description: 测试orc功能

Copyright (c) 2022 by bob, All Rights Reserved. 
'''
import easyocr
ocr=easyocr.Reader(['ch_sim','en'])

test_list=ocr.readtext(r'C:\Users\liaoyan\Downloads/1234.png',detail=0)
print(test_list)
