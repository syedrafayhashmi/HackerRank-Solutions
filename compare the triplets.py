#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ascore = 0
    bscore = 0 
    for x in enumerate(a):
        if x[1] > b[x[0]]:
            ascore += 1
        if x[1] < b[x[0]]:
            bscore += 1
    return ascore,bscore

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
