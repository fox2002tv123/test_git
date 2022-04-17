'''
Author: bob
Date: 2022-04-17 18:39:55
LastEditors: bob
LastEditTime: 2022-04-17 18:47:22
FilePath: \test_git\test_git\test_rpa.py
Description: 

Copyright (c) 2022 by bob, All Rights Reserved. 
'''
import rpa as r
r.init()
r.url('https://www.baidu.com') # 打开网页
# r.type('//*[@name="q"]', 'decentralisation[enter]') # 搜索
# print(r.read('result-stats')) # 读取结果
# r.snap('page', 'results.png') # 截图
# r.close() # 关闭网页

r.init(visual_automation = True, chrome_browser = True) # 初始化
print(r.read('pdf_window.png')) # 读取结果
print(r.read('image_preview.png')) # 读取结果
r.hover('anchor_element.png') # 鼠标移动到元素
print(r.read(r.mouse_x(), r.mouse_y(), r.mouse_x() + 400, r.mouse_y() + 200)) # 读取结果
r.close() # 关闭网页