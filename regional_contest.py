# N=4
# arr=[30, 5, 15, 22]
# N=int(input())
# arr = [int(x) for x in input().split()]
# # score = min(arr) - 1
# score = int(max(arr)/7)
# teams = sum(map(lambda x:int(x / score), arr))
# while teams>7:
#     score += 1
#     teams = sum(map(lambda x:int(x / score), arr))
#     # print('score',score,'teams',teams)
# print(score-1)

N=int(input())
arr = [int(x) for x in input().split()]

def check(score):
    if  sum(map(lambda x: x // (score), arr)) > 7:
        return False
    return  True

def Binary_search(l, r):
    if l==r: return l
    mid = (l+r)//2
    if check(mid):
        return Binary_search(l,mid)
    return Binary_search(mid+1, r)
lower = 1
upper = (10**9) + 47
print(Binary_search(lower, upper) -1)




# score = len(arr)
# while True:
#     score2 = score ** len(arr)
#     teams1 = sum(map(lambda x: int(x / score), arr))
#     teams2 = sum(map(lambda x: int(x / score2), arr))
#     if teams1 <= 7:
#         break
#     if teams2 > 7:
#         score = score2
#     else:
#         score += 1
#     # print('score',score,'teams',teams)
# print(score-1)