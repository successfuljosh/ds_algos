N = int(input())
Ingre = [int(x) for x in input().split(' ')]
#sort array
Ingre.sort()
for i in range(0, N - 1):
	Ingre[i+1] = (Ingre[i] + Ingre[i + 1]) / 2
print(Ingre[N-1])