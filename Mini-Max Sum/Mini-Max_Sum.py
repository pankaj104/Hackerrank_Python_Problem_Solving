#!/bin/python3

arr=list(map(int, input().split()) )
arr.sort()
n= len(arr)
total=0
for i in range(0,n):
   total=total+arr[i]
    
print(total-arr[n-1], total-arr[0])

