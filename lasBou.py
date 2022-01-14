# def min_amt(K, T, A):
#     if (K >= 1 and K <= 5000):
#         if (T >= 1 and T <= 10 ** 5):
#             P = 0
#             if T <= K:
#                 for j in range(len(A)):
#                     P = P + (A[j] + T)
#             elif T > K:
#                 P = P + max(A) * K + T
#     return P


k, t = input().split(" ")
A = input().split(" ")

K = int(k)
T = int(t)
A = [int(i) for i in A]
A.sort()
P = 0
if (K >= 1 and K <= 5000):
    if (T >= 1 and T <= 10 ** 5):
        if T <= K:
            for j in range(len(A)):
                P = P + (A[j] + T)
        elif T > K:
            P = P + max(A) * K + T
print(P)