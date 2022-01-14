def removeDuplicates(self, s: str, k: int) -> str:
    dic = dict()
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    for (key, v) in dic.items():
        dic[key] = v % k

    ans = {i: dic[i] for i in dic if dic[i] != 0}
    l = [a * ans[a] for a in ans]

    return ''.join(l)
#
#
# s = "deeedbbcccbdaa"
# l=[]
# l[:0] =s
# print(l)
# b='d'
# i=0
# while i<len(l):
#     # print(i,l[i])
#     if l[i] == b:
#         l.remove(l[i])
#         l.remove(l[i+1])
#     print(i,l[i])

k=8
while True:
    i = -3
    while i< k:
        # print(i)
        i += 1
        if i == 4:
            print('break')
            break