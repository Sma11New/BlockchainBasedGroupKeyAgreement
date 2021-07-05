#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author   : Cr4y0n
# @Software : PyCharm
# @Time     : 2021/07/03
# @Github   : https://github.com/Cr4y0nXX

from createKey import createKey, genPrimeNumber
from keyAgreement import GKA
from block import Block
import random

# 手动输入区块信息
def inputMsg():
    pubKey_n, pubKey_e, priKey = 0, 0, 0
    try:
        pubKey_n = int(input("公钥n: "))
        pubKey_e = int(input("公钥e: "))
        priKey = int(input("私钥d: "))
    except:
        print("请输入正整数！")
    return pubKey_n, pubKey_e, priKey

# 添加区块到区块链
def addBlock(pubKeyList, blockList, number, pubKey_n, pubKey_e, priKey, primeNumber):
    blockKeyDic = {}
    blockKeyDic["pubKey_n"] = pubKey_n
    blockKeyDic["pubKey_e"] = pubKey_e
    blockKeyDic["primeNumber"] = primeNumber
    pubKeyList.append(blockKeyDic)
    block = Block(number + 1, pubKey_n, pubKey_e, priKey, primeNumber)
    blockList.append(block)
    return pubKeyList, blockList

# 验证区块
def verifyBlock(pubKeyList, blockList, number):
    try:
        msg = str(random.randint(10000, 1000000))
        print("=============区块验证=============")
        print(f"区块 {number - 1} 验证区块 {number}")
        print(f"区块 {number} 公钥：n {pubKeyList[-1]['pubKey_n']} || e {pubKeyList[-1]['pubKey_e']}")
        print("验证明文：", msg)
        cipherText = blockList[-2].encrypt(pubKeyList[-1]["pubKey_n"], pubKeyList[-1]["pubKey_e"], msg)
        print("公钥加密：", cipherText)
        text = blockList[-1].decrypt(cipherText)
        print("私钥解密：", text)
        print("==================================")
        if text != msg:
            print(">>> 验证错误，添加失败！")
            return False
        else:
            print(">>> 成功添加！")
            return True
    except:
        print(">>> 验证错误，添加失败！")
        return False

def printBlock(number):
    for i in range(number):
        print(f"--------------\033[32mblock {i + 1}\033[0m--------------")
        print("| 编号  |", blockList[i].number)
        print("| 公钥n |", blockList[i].pubKey_n)
        print("| 公钥e |", blockList[i].pubKey_e)
        print("| 素数  |", blockList[i].primeNumber)
        # print("私钥 ", blockList[i].priKey)
        print("| 时间  |", blockList[i].creatTime)
    print(f"-----------------------------------")
    print(f"\033[31m总区块数：{number}\033[0m\n")

def printMenu():
    menu = """
                ---------基于RSA的区块链群组密钥协商---------
                |       add         |      手动添加区块     |
                |        0          |      协商群组密钥     |
                |      other        |      自动生成区块     |
                --------------------------------------------
     """
    print(f"\033[36m{menu}\033[0m")

if __name__ == "__main__":
    pubKeyList = []
    blockList = []
    primeNumberList = []
    number = 0
    printMenu()
    while number + 1:
        try:
            a = input("> ")
        except KeyboardInterrupt:
            print("\nBye~\n")
            exit(0)
        if a == "add":
            pubKey_n, pubKey_e, priKey = inputMsg()
            if not pubKey_n and not pubKey_e and not priKey:
                continue
        elif a == "0":
            GKA(primeNumberList)
            exit(0)
        else:
            pubKey_n, pubKey_e, priKey = createKey()
        primeNumber = genPrimeNumber(1, 5)
        pubKeyList, blockList = addBlock(pubKeyList, blockList, number, pubKey_n, pubKey_e, priKey, primeNumber)  # 添加区块
        primeNumberList.append(primeNumber)
        number += 1
        if len(blockList) >= 2:
            if not verifyBlock(pubKeyList, blockList, number):
                number -= 1
                pubKeyList.pop()
                blockList.pop()
                primeNumberList.pop()
        printBlock(number)
