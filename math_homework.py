n,c = input().split()
n = int(n)
c = int(c)
limit = int((c-1)**(1/n))

#brute
# for i in range(1, limit+1):
#     for j in range(1, limit+1):
#         if math.pow(i,n) + math.pow(j,n) == c:
#             pairs.append((i,j))
# temp_arr = [x**n for x in range(1,limit+1)]
count=0


if n>1:
    temp_arr = {x**n:1 for x in range(1,limit+1)}
    # pairs = []

    for j in range(1, limit+1):
        diff = c - (j ** n)
        if diff in temp_arr:
            count +=1
            # a_i = temp_arr.index(diff)+1
            # pairs.append((a_i,j))

else:
    count = c-1

# print(len(pairs))
print(count)
