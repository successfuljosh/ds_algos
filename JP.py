st='''aAPPLY
ahhsg

aggsu
AJDJD'''
#
# sd = st.split('\n')
# print(sd)
# val = sd[0].lower()
# u=0
# while u < len(sd):
#     if sd[u]:
#         val += sd[u].capitalize()
#     else:
#         u +=1
#     u+=1
#
# print(val)

# st = 'xtneiootnrnoeneeeeuoeoheetehounzoiuetrhfefeezuivirfwieotgoottfnrnneghetserhrwsgesfherhtiitrerevreernhveo'
# strr=''.join(sorted(st))
# print('eno' in strr)
#
# dd = [2,3,1,5,7,4]
# dd = sorted(dd)
# print(''.join(dd))

import sys

n, k = sys.stdin.readline().split()
A = sys.stdin.readline().split()
cool = 0
cct = 0
for a in A:
    if int(a) >= int(k):
        cool +=1
    else:
        if cct < cool:
            cct = cool
        cool = 0

print(cct)
