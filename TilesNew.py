N = int(input())
A = [int(x) for x in input().split(' ')]
B = [int(x) for x in input().split(' ')]
C = [int(x) for x in input().split(' ')]
A_sum = sum(A)
B_sum = sum(B)
C_sum = sum(C)
s1 = s2 = s3 = 0
i = 0
while(i<N):
    #find the minimum of all combination and sumup
    s1 += min(A[i], B[i])
    s2 += min(C[i], B[i])
    s3 += min(A[i], C[i])
    i+=1

min_sum_cost = min(s1, s2, s3)
overall_min_cost = min(min_sum_cost,A_sum, B_sum, C_sum )
print(overall_min_cost)