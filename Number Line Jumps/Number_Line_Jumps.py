#!/bin/python3

import math
import os
import random
import re
import sys



def kangaroo(x1, v1, x2, v2):
   
       
    x= x1-x2
    v= v2-v1
    
    
    
        
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        if v== 0:
            return 'NO'
        else:
            result = x % v
            if result == 0:
                return 'YES'
            else:
                return 'NO' 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
