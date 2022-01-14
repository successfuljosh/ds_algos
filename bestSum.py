#Search through all leaves and return valid array the shortest depth
def best_sum(target, numbers):
    if target == 0: return []
    if target < 0: return None

    shortest_combination = None
    for i in numbers:
        remainder = target - i
        combination = best_sum(remainder, numbers)
        if combination != None:
            new_combination = combination + [i]  #creates a copy of the combination and appending the newe value 'i'
            if shortest_combination == None or len(new_combination) < len(shortest_combination):
                shortest_combination = new_combination
    return shortest_combination
'''
time complexity = O(n^m * m)
space complexity = O(m*m)   the 2nd m is as a result of the size of the shortest_combination array
'''



#Optimizing using memoization
def best_sum_memo(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortest_combination = None
    for i in numbers:
        remainder = target - i
        combination = best_sum_memo(remainder, numbers, memo)
        if combination != None:
            new_combination = combination + [i]  #creates a copy of the combination and appending the newe value 'i'
            if shortest_combination==None or len(new_combination) < len(shortest_combination):
                shortest_combination = new_combination
                # memo[remainder] = shortest_combination
    memo[target] = shortest_combination
    return memo[target]

'''
time complexity = O(n * m * m)
space complexity = O(m*m)   the 2nd m is as a result of the size of the shortest_combination array
'''

print(best_sum(7,[5,2,3,4,7]))
print(best_sum(8,[1,4,5]))
# print(best_sum(100,[1,2, 5,2]))
print(best_sum_memo(100,[1,2,5,25]))
print(best_sum_memo(300,[7, 14]))
