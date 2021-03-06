'''
Author: bob
Date: 2022-04-10 18:17:14
LastEditors: bob
LastEditTime: 2022-04-15 16:27:44
FilePath: \test_git\test_git\pywebIO_OK.py
Description: 测试通过

Copyright (c) 2022 by bob, All Rights Reserved. 
'''
from asyncio import start_server
from pywebio.input import input, FLOAT # 导入输入
from pywebio.output import put_text

def bmi(): # 计算BMI
    height = input("请输入你的身高(cm)：", type=FLOAT)
    weight = input("请输入你的体重(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2 # 计算BMI

    top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
                  (22.9, '正常'), (27.5, '过重'),
                  (40.0, '肥胖'), (float('inf'), '非常肥胖')]
    # 判断BMI状态
    for top, status in top_status:
        if BMI <= top:
            put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
            break

if __name__ == '__main__':
    bmi()
    # start_server(bmi, port=80)