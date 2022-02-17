
def num_freq(arr):
    d = {}
    #O(n)
    for a in arr:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    new_d = {}
    for k, v in d.items():
        if v in new_d:
            temp = new_d[v]
            temp.append(k)
            new_d[v] = temp
        else:
            t = [k]
            new_d[v] = t
    #sort new_d by keys, and then sort the inner values
    #O(nlogn)
    new_d = dict(sorted(new_d.items(), key=lambda x: x[0], reverse=True))
    new_d = {k:sorted(v) for k, v in new_d.items()}

#O(n*rt(n))
    final_arr = []
    for freq,nums in new_d.items():
        for x in nums:
            final_arr.append([x,freq])
    return final_arr



print(num_freq([3,3,5,1,3,1,2,1]))