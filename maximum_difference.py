#!/bin/python

import sys
import os

# Complete the function below.


def  maxDifference( a):
    largest = -1000000
    smallest = 1000000
    li = 0
    for x in range(0, len(a)):
        if a[x] > largest :
            largest = a[x]
            li = x
    for x in range(0, li):
        if a[x] < smallest:
            smallest = a[x]
    return largest - smallest

f = open(os.environ['OUTPUT_PATH'], 'w')
    

_a_cnt = 0
_a_cnt = int(raw_input())
_a_i=0
_a = []
while _a_i < _a_cnt:
    _a_item = int(raw_input());
    _a.append(_a_item)
    _a_i+=1
    

res = maxDifference(_a);
f.write(str(res) + "\n")

f.close()
