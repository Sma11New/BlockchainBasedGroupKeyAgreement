#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author   : Cr4y0n
# @Software : PyCharm
# @Time     : 2021/07/03
# @Github   : https://github.com/Cr4y0nXX

from createKey import sushu

#快速指数算法的模冥运算
#a**b%c
def moming(a1,b1,c1):
    b=1
    while b1>0:
        a=b1%2
        if a==1:
            b=a1*b%c1
        a1=a1*a1%c1
        b1=int(b1/2)
    return b

# 生成本元根
def yuangeng(a):
    for i in range(2, 10):
        if moming(i, a - 1, a) == 1:
            return i

# 密钥协商协议
# key=GKA(n,g)
def GKA(a):
    primeTmp = sushu(1, 10)
    g = yuangeng(primeTmp)
    x = a
    print("\n各个成员依次选取的协商整数：", x, "\n")
    v = 1
    for i in range(len(x)):
        v *= x[i]
        c = g ** v
        if i + 1 != a:
            print("Block%d -> Block%d 传递 %d" % (i, i + 1, c))
        # 输出函数的槽填入输出
        else:
            print("Block%d -> Block%d 传递 %d" % (i, 0, c))
    print(f"\n\033[31m协商出的密钥为：{c}\033[0m\n")
    return c


