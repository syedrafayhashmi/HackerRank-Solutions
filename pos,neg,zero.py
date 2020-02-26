#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arr = arr
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for x in arr:
    
        if x > 0:
            pos+=1
        if x < 0:
            neg+=1
        if x == 0:
            zero+=1
    return pos/total,neg/total,zero/total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)
    fptr.write('\n'.join(map(str, result)))
    fptr.close()