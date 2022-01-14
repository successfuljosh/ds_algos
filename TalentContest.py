#search by boxes
#return true if there are empty squares

def is_empty_squares(arr,i,j,n_squares, k_limit):
    ones=0
    if i+n_squares> len(arr) or j+n_squares> len(arr[i]):
        return False
    for r in range(i, i+n_squares):
        for c in range(j, j+n_squares):
            ones+=arr[r][c]
    # print(ones)
    if ones <= k_limit:
        return True
    return False


# array = [[1, 0, 1, 1],
#          [0,0,0,0],
#          [0,0,1,0],
#          [1,0,0,0]]
# N = 4
# K =1

N,K = [int(x) for x in input().split()]
array = []
for a in range(N):
    # row = [ord(x)-ord('0') for x in input()]
    row = [int(x) for x in input()]
    array.append(row)
# print(array, N, K)
result = []
for n in range(N,0,-1):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if is_empty_squares(array, i, j, n, K):
                result.append(n)
if len(result)>0:
    print(max(result))
else:
    print(0)



