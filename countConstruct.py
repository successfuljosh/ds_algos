#recursive methods for string data

def count_construct(target, word_bank):
    #base case
    if target == '': return 1
    total_count = 0
    for word in word_bank:
        #check if word is a prefix to target
        if word not in target: continue
        if target.index(word)==0:
            suffix = target.replace(word, '',1)
            inner_count = count_construct(suffix, word_bank)
            total_count += inner_count
    return total_count

#memoizing
def count_construct_memo(target, word_bank, memo={}):
    if target in memo: return memo[target]
    #base case
    if target == '': return 1
    total_count = 0
    for word in word_bank:
        #check if word is a prefix to target
        if word not in target: continue
        if target.index(word)==0:
            suffix = target.replace(word, '',1) #max of O(m)
            inner_count = count_construct_memo(suffix, word_bank, memo)
            total_count += inner_count
    memo[target] = total_count
    return total_count

'''Complexities
BRUTE FORCE METHOD
m = target length
n = wordBank length
time = O(n^m * m)
space = O(m^2)

MEMOIZED METHOD
m = target length
n = wordBank length
time = O(n * m * m)
space = O(m^2)
'''

print(count_construct('purple', ['purp', 'p','ur','le','purpl']))  #2
print(count_construct('abcdef', ['ab', 'abc','cd','def','abcd']))   #1
print(count_construct('stakeboard', ['bo','rd','ate','t','sta','sk','boar']))  #0
print(count_construct_memo('enterapotentpot', ['a','p','ent','enter','ot','o','t']))  #4
print(count_construct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                    ['e','ee','eee','eeee','eeeee', 'eeeeee','eeeeeee',
                     'eeeeeeee','eeeeeeeee','eeeeeeeeee']))  #0

