N,M = input().split()
N,M =int(N), int(M)

N *= M
if (N % 2 == 0):
    print("Dragon")
else:
    print("Imp")