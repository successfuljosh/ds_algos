#intervals = [[1,3],[2,6],[8,10],[15,18]]
#we sort the intervals by the first item  time = O(nlogn)
#then we create merged array time and space = o(n)



def mergeIntervals(list_intervals):
    merged= []
    list_intervals = sorted(list_intervals, key=lambda x:x[0])
    for interval in list_intervals:
        #add interval to merged if merged is empty or if interval is not part of the last merge interval
        if len(merged)==0 or merged[-1][1] < interval[0]:
            merged.append(interval)
        else: #update the overlap-
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]
merged = mergeIntervals(intervals)

print(intervals)
print(merged)