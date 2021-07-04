#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author   : Cr4y0n
# @Software : PyCharm
# @Time     : 2021/07/03
# @Github   : https://github.com/Cr4y0nXX

import time

# 区块类
class Block:
    def __init__(self, number, pubKey_n, pubKey_e, priKey, primeNumber):
        self.number = number
        self.pubKey_n = pubKey_n
        self.pubKey_e = pubKey_e
        # self.priKey = priKey
        self.__priKey = priKey  # 私钥设定为私有属性
        self.primeNumber = primeNumber
        self.creatTime = time.asctime(time.localtime(time.time()))

    # 解密，被验证
    def decrypt(self, ciphertextList):
        plaintext = ""
        for item in ciphertextList:
            # plaintext += str((item ** self.priKey % self.pubKey_n))
            plaintext += str((item ** self.__priKey % self.pubKey_n))
        return plaintext

    # 加密，验证其它区块
    def encrypt(self, n, e, plaintext):
        plaintextList = []  # 分组后的明文列表
        ciphertextList = []  # 密文列表
        i = 0
        # 按n的位数减位判断
        while i < len(plaintext):
            j = len(str(n))
            while True:
                if int(plaintext[i:(i + j)]) < n:
                    plaintextList.append(int(plaintext[i:(i + j)]))
                    i += j
                    break
                j -= 1
        # 加密
        for item in plaintextList:
            cipherText = item ** e % n
            ciphertextList.append(cipherText)
        return ciphertextList

# if __name__ == "__main__":
#         a = Block(1, 2, 3)

