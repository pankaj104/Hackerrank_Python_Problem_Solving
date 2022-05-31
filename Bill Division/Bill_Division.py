#!/bin/python3

import math
import os
import random
import re
import sys



def bonAppetit(bill, k, b):
    sum1=0
      
    for i in range(0,n):
        if( i!=k):
            sum1= sum1+bill[i]
    
     
    bactual= int(sum1/2  )     
    if (b> bactual):
        print (b-bactual)
    else:
        print ("Bon Appetit")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

