N = int(input())
# no_ways = [[0] * 4 for i in range(N + 1)]
no_of_ways=[]
for i in range(N+1):
    no_of_ways.append([0, 0, 0, 0])

lift = 0
while lift<N+1:
    for count in range(4):
        if lift != 0:
            for step in range(1, 4):
                if step != count and step <= lift:
                    no_of_ways[lift][count] += no_of_ways[lift - step][step]
        else:
            no_of_ways[lift][count] = 1
    lift+=1
print(no_of_ways[-1][0])








