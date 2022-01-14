# first = [int(x) for x in input().split()]
# N,M = first[0], first[1]
# pairs = []
# for i in range(M):
#     p = [int(s) for s in input().split()]
#     pairs.append(p)
#
# # N,M = 6, 5
# # pairs = [[1, 2],
# #          [2, 3],
# #          [4, 5],
# #          [2, 1],
# #          [1, 3]]
#
# constel = {}
# bucket = {}
# constel[0] = pairs[0]
# bucket[0] = 1
#
# star_set={pairs[0][0],pairs[0][1]}
#
# def searchforkey(dict, q):
#     for b,v in dict.items():
#         if q in v:
#             return b
#     return -1
#
# for i in range(1,M):
#     p = pairs[i]
#     key = searchforkey(constel, p[0])
#     if key == -1:
#         key = searchforkey(constel, p[1])
#     if key != -1:
#         va = constel[key]
#         va.extend(p)
#         bucket[key] += 1
#     else:
#         index = len(constel)
#         constel[index] = p
#         bucket[index] = 1
#     star_set.add(p[0])
#     star_set.add(p[1])
#
# all = {x for x in range(1, N+1)}
# diff = all.difference(star_set)
#
# for a in diff:
#     index = len(constel)
#     constel[index] = []
#     bucket[index] = 0
# # if len(diff)>0:
# #     index = len(constel)
# #     constel[index] = []
# #     bucket[index] = 0
#
# print(len(constel))
# constellations = list(bucket.values())
# constellations.sort()
# for k in constellations:
#     print(k)


#ANOTHER IDEA

N,M = 6, 5
pairs = [[1, 2],
         [2, 3],
         [4, 5],
         [2, 1],
         [1, 3]]

def same_constellation(i,j):
    for p in pairs:
        if i in p and j in p:
            return True
    return False

class Levelpair:
    def __init__(self, pair):
        self.level=1
        self.pairs=pair


all = [i for i in range(1, N + 1)]
all_set = {i for i in range(1, N + 1)}
K = 0
pair_list = []
for i in range(len(all)):
    for j in range(len(all)):
        # check if in same constellation
        if same_constellation(all[i], all[j]):
            if len(pair_list)>0:
                for lp in pair_list:
                    if all[i] in lp.pairs or all[j] in lp.pairs:
                        lp.pairs.add(all[i])
                        lp.pairs.add(all[j])
                        lp.level += 1
                    else:
                        new_set = set()
                        new_set.add(all[i])
                        new_set.add(all[j])
                        pair_list.append(Levelpair(new_set))
            else:
                new_set = set()
                new_set.add(all[i])
                new_set.add(all[j])
                pair_list.append(Levelpair(new_set))

hh=set()
for a in pair_list:
    hh = hh.union(a.pairs)
diff = all_set.difference(hh)
last = Levelpair(diff)
last.level = 0
pair_list.append(last)

for a in pair_list:
    print(a.level, a.pairs)