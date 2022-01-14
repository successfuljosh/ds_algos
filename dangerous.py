import sys

receive = input().split(' ')
N = int(receive[0])
A = int(receive[1])
B = int(receive[2])

dynamitTiles = input()

seconds = sys.maxsize

kovalskiCan = [0 for i in range(N)]
ricoCan = [0 for i in range(N)]

ricoStart = A
kovalskiStart = B

while (ricoStart >= 1):
    if (dynamitTiles[ricoStart - 1] == '1'):
        ricoCan[ricoStart - 1] = 1
        ricoStart -= 4
    else:
        break

while (kovalskiStart >= 1):
    if (dynamitTiles[kovalskiStart - 1] == '1'):
        kovalskiCan[kovalskiStart - 1] = 1
        kovalskiStart -= 7
    else:
        break

ricoStart = A
kovalskiStart = B

while (ricoStart <= N):
    if (dynamitTiles[ricoStart - 1] == '1'):
        ricoCan[ricoStart - 1] = 1
        ricoStart += 4
    else:
        break

while (kovalskiStart <= N):
    if (dynamitTiles[kovalskiStart - 1] == '1'):
        kovalskiCan[kovalskiStart - 1] = 1
        kovalskiStart += 7
    else:
        break

for i in range(N):
    if (ricoCan[i] == 1 and kovalskiCan[i] == 1):
        seconds = min(seconds, abs(i + 1 - A) / 4 + abs(i + 1 - B) / 7)
if (seconds == sys.maxsize):
    print(-1)
else:
    print(seconds)
