mystring='hhtte thy hello boy'
_, _, ans = mystring.partition('thy')
print(ans)

def rec_russian(a,b):
    if a==0: return 0
    if a%2==0: return 2 * rec_russian(a/2,b)
    if a%2 != 0: return b + 2 * rec_russian((a-1)/2, b)

print(rec_russian(38,3))


import re
found = re.search('Tthy [A-Z]', mystring)
print(found)