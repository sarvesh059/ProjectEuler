#!/bin/python3

import sys

def calc(n,x):
    r = (n-1)//x
    return int((x*r*(r+1))>>1)  # Here, we use shift right instead of dividing by 2 because converting float to int will lead to some degree of error in calculation

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(calc(n,3)+ calc(n,5) - calc(n,15))
