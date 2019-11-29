# -*- coding: utf-8 -*-
# @author: lenovo 
# @email: wangyufan@shanshu.ai 
# @date: 2019/11/27
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import random

def genSizeFile(fileName, fileSize):
    #file path
    filePath="./dataset/Data"+fileName+".txt"

    # 生成固定大小的文件
    # date size
    ds = 0
    with open(filePath, "w", encoding="utf8") as f:
        while ds < fileSize:
            char = random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
            f.write(str(char))
            # f.write("\n")
            ds=os.path.getsize(filePath)
    # print(os.path.getsize(filePath))

# start here.


for i in range(20):
    temp_name = str(i+1) + "M"
    temp_size = (i+1) * 1024 *1024
    print(i+1)
    genSizeFile(temp_name,temp_size)