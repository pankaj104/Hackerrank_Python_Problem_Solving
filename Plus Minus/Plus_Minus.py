#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    a=0
    b=0
    c=0
    # Write your code here
    for i in range(0,n):
        if(arr[i]>0):
            a=a+1
        elif(arr[i]<0):
            b=b+1
        else:
            c=c+1
    print("%.6f"%(a/n))
    print("%.6f"%(b/n))
    print("%.6f"%(c/n))     
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
