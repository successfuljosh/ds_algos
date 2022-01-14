
def how_sum(target, numbers):
    if target == 0: return []
    if target < 0: return None
    for i in numbers:
        remainder = target - i
        combination = how_sum(remainder, numbers)
        if combination != None:
            combination.append(i)
            return combination
    return None

#memoized method
def how_sum_memo(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    for i in numbers:
        remainder = target - i
        combination = how_sum_memo(remainder, numbers, memo)
        if combination != None:
            combination.append(i)
            memo[remainder] = combination
            return combination
    memo[target] = None
    return None

# print(how_sum_memo(7,[5,2,3,4,7]))
# print(how_sum_memo(300,[7, 14]))
print(how_sum_memo(4,[1,2,3,4]))
