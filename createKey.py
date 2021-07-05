#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author   : Cr4y0n
# @Software : PyCharm
# @Time     : 2021/07/03
# @Github   : https://github.com/Cr4y0nXX

import random
from algorithm import getInverse      # 求逆元
from algorithm import judgeCoPrime    # 判断互素
from algorithm import genPrimeNumber  # 模幂运算

# 产生密钥（n，e为公钥，d为私钥）
def createKey():
    p = genPrimeNumber(100, 1000)
    q = genPrimeNumber(100, 1000)
    n = p * q
    n_Euler = (p - 1) * (q - 1)
    while True:
        # e = int(input("选择公钥e（1 < e < %d 且e与%d互质）：" %(n_Euler, n_Euler)))
        e = random.randint(1, n_Euler)
        # print("e: ", e)
        if 1 < e < n_Euler and judgeCoPrime(e, n_Euler):
            break
    d = getInverse(e, n_Euler)
    return n, e, d

