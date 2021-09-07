#!/bin/python3

import math
import os
import random
import re
import sys



def countApplesAndOranges(s, t, a, b, apples, oranges):
    x=0
    y=0
    for i in range(0,m):
        apples[i]= apples[i]+a
        if((apples[i]>=s) & (apples[i]<=t)):
            x=x+1
        
    print (x) 
    for j in range(0, n):
        oranges[j]= oranges[j]+b
        if((oranges[j]>=s) & (oranges[j]<=t)):
            y=y+1
        
    
    print(y)        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

