#binary search: works for sorted list, has O(logn) time complexity
#recursive Method
def binary_recursive(array, target, left, right):
    #check
    if left>right:
        return False

    mid = int((left+right)/2)
    #OR
    mid = int(left + (right - left)/2)

    if array[mid] == target:
        return True

    if array[mid] > target:
        #ignore the right side of the array
        return binary_recursive(array, target,left, mid-1)
    else:
        #ignore the left side of the array
        return binary_recursive(array,target, mid+1,right)

#ITERATIVE METHOD
def binary_iterative(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int(left+(right-left)/2)
        if array[mid] == target:
            return True
        if array[mid] > target:
    # ignore the right side of the array
            right = mid -1
        else:
            left = mid +1
    return False

array = [1,3,8,10,23,90,56]
target = 10

print(binary_recursive(array,target,0,len(array)-1))
print(binary_iterative(array,target))