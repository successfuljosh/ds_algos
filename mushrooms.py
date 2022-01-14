
# n,max_weights = [int(x) for x in input().split()]
# buckets = [int(x) for x in input().split()]
# buckets.sort()
# ways=set()
# for x in buckets:
#     if x<= max_weights:
#         ways.add(x)
#
# for i in range(n):
#     for j in range(i+1, n):
#         addi = buckets[i]+buckets[j]
#         if addi <= max_weights:
#             ways.add(addi)
# print(len(ways))


#Search through all leaves and return valid array the shortest depth
def count_construct(target, numbers_bank):
    #base case
    if target == 0: return 1
    total_count = 0
    for word in numbers_bank:
        #check if word is a prefix to target
        if word > target: continue
        remainder = target - word
        inner_count = count_construct(remainder,numbers_bank)
        numbers_bank.remove(word)
        total_count += inner_count
    return total_count

print(count_construct(7, [5, 2, 3, 4, 7]))
print(count_construct(10, [1, 4, 8]))
