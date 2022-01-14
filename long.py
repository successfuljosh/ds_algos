def all_construct(target, numbers):
    #base case
    if target == 0: return [[]]
    if target < 0: return None
    all_arrays = []
    for i in numbers:
        #check if word is a prefix to target
        # if word not in target: continue
        suffix = target - i
        last_array = all_construct(suffix, numbers)
        if last_array !=None:
            arrays = [[i] + suf for suf in last_array]
            all_arrays += arrays
    return all_arrays

nk = input().split(' ')
N = int(nk[0])
K = int(nk[1])
array = [i for i in range(N+1)]
print(all_construct(N, array))

