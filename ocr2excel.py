'''
Author: bob
Date: 2022-04-11 13:08:46
LastEditors: bob
LastEditTime: 2022-04-11 13:32:46
FilePath: \test_git\ocr2excel.py
Description: 将图片文字提取到excel中

Copyright (c) 2022 by bob, All Rights Reserved. 
'''
import easyocr
import xlwings as xw
import os

# 图片文件夹
root=r'C:\Users\liaoyan\Downloads/G'

# 创建ocr的reader对象,识别中英文，启用显卡
ocr=easyocr.Reader(['ch_sim','en'],gpu=True)  #?gpu=True

# 填充信息-图片必须英文名字
info_list=[]
for fn in os.listdir(root):
    text_list=ocr.readtext(f'{root}/{fn}',detail=0)
    info_list.append([text_list[0],text_list[1]])
    
# 写入工作簿
xw.Book().sheets(1).range('A1').value=info_list