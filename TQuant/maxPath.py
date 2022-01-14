def to_pyramid(node_val):
    arr = []
    count = 1
    while count<=len(node_val):
        arr.append(node_val[:count])
        del node_val[:count]
        count += 1
    return arr

def maximum_path(node_values):
    # Write your code here
    arr = to_pyramid(node_values)
    for row in range(len(arr)-2, -1, -1):
        for col in range(len(arr[row])):
            arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])
    return arr[0][0]
l = [1,3,-1,3,1,5]
print(maximum_path(l))
