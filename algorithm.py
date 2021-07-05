#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author   : Cr4y0n
# @Software : PyCharm
# @Time     : 2021/07/05
# @Github   : https://github.com/Cr4y0nXX

import random

# 判断素数
def judgePrimeNumber(num):
    # 不能被2~sqrt(m)（取整）之间的整数整除的数即素数
    sqrtResult = int(num **0.5)
    for i in range(2, sqrtResult + 1):
        if num % i  == 0:
            return False
    return True

# 判断互质
def judgeCoPrime(a, b):
    # 求最大公因数
    def maxCommonFactor(m, n):
        result = 0
        while  m % n > 0:
            result = m % n
            m = n
            n = result
        return result
    if maxCommonFactor(a, b) == 1:
        return True
    return False

# 生成本元根
def genPrimitiveRoot(a):
    for i in range(2, 10):
        if modularExponentiation(i, a - 1, a) == 1:
            return i

# 求逆元
def getInverse(a, b):
    # 扩展的欧几里得
    def extGcd(a_, b_, arr):
        if b_ == 0:
            arr[0] = 1
            arr[1] = 0
            return a_
        g = extGcd(b_, a_ % b_, arr)
        t = arr[0]
        arr[0] = arr[1]
        arr[1] = t - int(a_ / b_) * arr[1]
        return g
    # 求a模b的乘法逆x
    arr = [0,1,]
    gcd = extGcd(a, b, arr)
    if gcd == 1:
        return (arr[0] % b + b) % b
    else:
        return -1

#快速指数算法的模冥运算
#a**b%c
def modularExponentiation(a1, b1, c1):
    b = 1
    while b1 > 0:
        a = b1 % 2
        if a == 1:
            b = a1 * b % c1
        a1 = a1 * a1 % c1
        b1 = int(b1 / 2)
    return b

# 取指定范围内的一个素数
def genPrimeNumber(low, upper):
    primeList = []
    for num in range(low, upper + 1):
        # 素数大于 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primeList.append(num)
    return random.choice(primeList)

if __name__ == "__main__":
    pass
