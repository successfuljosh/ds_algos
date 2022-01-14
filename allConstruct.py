#recursive methods for string data

def all_construct(target, word_bank):
    #base case
    if target == '': return [[]]
    all_arrays = []
    for word in word_bank:
        #check if word is a prefix to target
        if word not in target: continue
        if target.index(word) == 0:
            suffix = target.replace(word, '',1)
            last_array = all_construct(suffix, word_bank)
            arrays = [[word]+suf for suf in last_array]
            all_arrays += arrays
    return all_arrays



def all_construct_memo(target, word_bank, memo={}):
    if target in memo: return memo[target]
    #base case
    if target == '': return [[]]
    all_arrays = []
    for word in word_bank:
        #check if word is a prefix to target
        if word not in target: continue
        if target.index(word) == 0:
            suffix = target.replace(word, '',1)
            last_array = all_construct_memo(suffix, word_bank, memo)
            arrays = [[word]+suf for suf in last_array]
            all_arrays += arrays

    memo[target] = all_arrays
    return all_arrays

'''Complexities
BRUTE FORCE METHOD === MEMOIZED METHOD.... NO MUCH OPTIMIZATION
m = target length
n = wordBank length
time = O(n^m * m) leaves/combination/subarrays
space = O(m) FOR SMALL DATA... BUT FOR LARGE DATA.... SPACE = O(n^m) 

MEMOIZED METHOD
m = target length
n = wordBank length
time = O(n * m * m)
space = O(m^2)
'''

print(all_construct_memo('purple', ['purp', 'p','ur','le','purpl']))  #2
print(all_construct('abcdef', ['ab', 'abc','cd','def','abcd']))   #[[abc,def]]
print(all_construct('stakeboard', ['bo','rd','ate','t','sta','sk','boar']))  #0
print(all_construct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))  #4
print(all_construct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                    ['e','ee','eee','eeee','eeeee', 'eeeeee']))  #0
