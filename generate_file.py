#-*- coding:utf-8 -*-
import os
import random

def genSizeFile(fileName, fileSize):
    
    #file path
    filePath="./dataset/Data"+fileName+".txt"

    # date size
    ds = 0
    with open(filePath, "w", encoding="utf8") as f:
        while ds < fileSize:
            char = random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
            f.write(str(char))
            ds=os.path.getsize(filePath)


for i in range(20):
    temp_name = str(i+1) + "M"
    temp_size = (i+1) * 1024 *1024
    print(i+1)
    genSizeFile(temp_name,temp_size)
