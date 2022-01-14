def step_cool(arra, K):
    for i in range(len(arra)):
        for j in range(i+1, len(arra)):
            if abs(arra[i]-arra[j]) > K:
                return False
    return True

def all_sum_memo(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return [[]]
    if target < 0: return None
    all_arrays = []
    for i in numbers:
        remainder = target - i
        combination = all_sum_memo(remainder, numbers, memo)
        if combination != None:
            arrays = [[i] + suf for suf in combination]
            all_arrays += arrays
    memo[target] = all_arrays
    return memo[target]

'''
time complexity = O(n * m * m)
space complexity = O(m*m)   the 2nd m is as a result of the size of the shortest_combination array
'''
N,K = [int(x) for x in input().split()]
# all = all_sum_memo(4, [1, 2, 3, 4])
all = all_sum_memo(N, [x for x in range(1,N+1)])
count=0
for s in all:
    if step_cool(s, K):
        count+=1
print(count)
print(len(all))