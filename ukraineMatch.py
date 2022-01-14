import math
n = int(input())
s = [int(x) for x in input().split(' ')]
low = min(s);
teams = [math.floor(x/low) for x in s]
while sum(teams)>7:
    low +=1
    teams = [math.floor(x / low) for x in s]
print(low)
