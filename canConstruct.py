#recursive methods for string data

def is_prefix(target, word):
    if word not in target: return False
    if target.index(word) == 0:
        return True
    return False


def can_construct(target, word_bank):
    #base case
    if target == '': return True
    for word in word_bank:
        #check if word is a prefix to target
        if is_prefix(target, word):
            suffix = target.replace(word, '',1)
            if can_construct(suffix, word_bank) == True:
                return True
    return False

'''Complexities
m = target length
n = wordBank length
time = O(n^m * m)
space = O(m^2)
'''

#optimized via memoization
def can_construct_memo(target, word_bank, memo={}):
    if target in memo: return memo[target]
    #base case
    if target == '': return True
    for word in word_bank:
        #check if word is a prefix to target
        if is_prefix(target, word):
            suffix = target.replace(word, '',1)
            if can_construct_memo(suffix, word_bank, memo) == True:
                memo[suffix] = True
                return True
    memo[target] = False
    return False

'''Complexities
m = target length
n = wordBank length
time = O(n * m * m)
space = O(m^2)
'''


print(can_construct('purple', ['purp', 'p','ur','le','purpl']))
print(can_construct('abcdef', ['ab', 'abc','cd','def','abcd']))
print(can_construct('stakeboard', ['bo','rd','ate','t','sta','sk','boar']))
print(can_construct_memo('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(can_construct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                    ['e','ee','eee','eeee','eeeee', 'eeeeee','eeeeeee',
                     'eeeeeeee','eeeeeeeee','eeeeeeeeee']))


