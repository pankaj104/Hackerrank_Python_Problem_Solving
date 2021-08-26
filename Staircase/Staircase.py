#!/bin/python3


n= int (input())
j=1
for i in range(n,0,-1):
    print(" "*(i-1)+("#"*j))
    j=j+1
