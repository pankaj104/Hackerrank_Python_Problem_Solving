
candles_count = int(input().strip())
n=0
candles = list(map(int, input().rstrip().split()))


maxlength= max(candles)
length= len(candles)

for i in range(0,length) :
    if(maxlength==candles[i]):
        n=n+1
       
    else:
        continue
print (n)

