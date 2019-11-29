# -*- coding: utf-8 -*-
from Crypto.Cipher import AES, Blowfish, DES
from Crypto import Random
import datetime
import os
import psutil
import os
import time as t
from struct import pack

def run_AES(plaintext):
    import pdb
    start = t.time()
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(plaintext)
    end = t.time()
    return (end - start)

def run_DES(plaintext):
    start = t.time()
    key = b'abcdefgh'
    iv = Random.new().read(DES.block_size)
    cipher = DES.new(key, DES.MODE_OFB, iv)
    msg = iv + cipher.encrypt(plaintext)
    end = t.time()
    return (end - start)

def run_blowfish(plaintext):
    start = t.time()
    bs = Blowfish.block_size
    key = b'An arbitrarily long key'
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    plen = bs - len(plaintext) % bs
    padding = [plen] * plen
    padding = pack('b' * plen, *padding)
    msg = cipher.iv + cipher.encrypt(plaintext + padding)
    end = t.time()
    return (end - start)

if __name__ == '__main__':
    time_list_AES = list()
    time_list_DES = list()
    time_list_Blow = list()
    for i in range(20):
        fileName = str(i + 1) + "M"
        filePath = "./dataset/Data" + fileName + ".txt"
        f = open(filePath)
        line = f.read()

        print("*" * 20 + "AES" + "*" * 20)
        total = 0
        for j in range(50):
            result = run_AES(line.encode("utf8"))
            total = result + total
        avg_time = total / 50
        time_list_AES.append(avg_time)
        info = psutil.virtual_memory()
        print (u'Memory Usage：', psutil.Process(os.getpid()).memory_info().rss)

        print("*" * 20 + "DES" + "*" * 20)
        total = 0
        for j in range(50):
            result = run_DES(line.encode("utf8"))
            total = result + total
        avg_time = total / 50
        time_list_DES.append(avg_time)
        info = psutil.virtual_memory()
        print (u'Memory Usage：', psutil.Process(os.getpid()).memory_info().rss)

        print("*" * 20 + "Blowfish" + "*" * 20)
        total = 0
        for j in range(50):
            result = run_blowfish(line.encode("utf8"))
            total = result + total
        avg_time = total / 50
        time_list_Blow.append(avg_time)
        info = psutil.virtual_memory()
        print (u'Memory Usage：', psutil.Process(os.getpid()).memory_info().rss)

    print(time_list_AES)
    print(time_list_DES)
    print(time_list_Blow)


