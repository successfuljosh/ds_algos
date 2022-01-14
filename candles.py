import math
N,M = [int(x) for x in input().split()]
candle_length=[int(s) for s in input().split()]
l=h=0
for i in range(M):
    if candle_length[i]>h:
        h=candle_length[i]

h+=1

tol=10**(-10)
result = 0
while(h-l)>tol:
    count = 0
    middle =(h+l)/2
    for i in range(M):
        count += math.floor(candle_length[i]/middle)
    if count>=N:
        l = middle
        result = middle
    if(count<N):
        h=middle

print(result)
