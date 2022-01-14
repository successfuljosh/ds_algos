#uses recursion and memoization
def can_sum(target, numbers):
    if target == 0: return True
    if target < 0: return False
    for i in numbers:
        remainder = target - i
        if can_sum(remainder, numbers) == True:
            return  True
    return False

#memoized method
def can_sum_memo(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False
    for i in numbers:
        remainder = target - i
        if can_sum_memo(remainder, numbers, memo) == True:
            memo[remainder] = True
            return  True
    memo[target] = False
    return memo[target]

#
print(can_sum_memo(7,[5,3,4,7]))
print(can_sum_memo(7,[2,4]))
print(can_sum_memo(300,[7,14]))


