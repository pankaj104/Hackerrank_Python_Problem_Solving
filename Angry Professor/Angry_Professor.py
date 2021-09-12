#!/bin/python3

import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    for i in range(0,t):
        u=0
        for j in range(0,n):
            if (a[j]<=0):
                u=u+1
        if (u>=k):
            
            return "NO"
        else:
            
            return "YES"
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()

