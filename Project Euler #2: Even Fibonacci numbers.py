#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n<= 1:
        print(0)
    else:
        result = 0
        f= 0
        s= 1
        temp = 0
        while temp<=n:
            temp = f+s
            f,s = s,temp
            if temp%2 == 0 and temp <=n:
                result += temp
        print(result)
