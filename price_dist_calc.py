
# import math as mt
# def cal_price(x,k,r):
#     circum = 2 * mt.pi * r
#     distance = circum * k
#     price = distance * x
#     return price
#
# X, K, R = [float(x) for x in input().split()]
# print(cal_price(X,K,R))
#
# N = int(input())
# list1 = [x for x in input().split()]
# list2 = [x for x in input().split()]
# L = [list1[-i] for i in range(1, N + 1)]
# if L == list2:
#     print('Yes')
# else:
#     print('No')
#     print(' '.join(L))

n = int(input())
l1 = [x for x in input().split()]
l2 = [x for x in input().split()]

def pap(n, l1,l2):
    L = [l1[len(l1)-i] for i in range(1,n+1)]
    if L == l2:
        return "Yes",None
    else:
        return 'No', L
result,LL = pap(n,l1,l2)
if result=='Yes':
    print(result)
else:
    print(result)
    print(' '.join(LL))