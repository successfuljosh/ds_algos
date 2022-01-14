import graphTraversal
#QUicksort has O(nlogn) runtime complexity..

def partition(array, left, right, pivot):
    def swap(arr, l, r):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1

    return left



def quicksort_implement(array, left, right):
    if left >= right:
        return

    pivot = array[int((left+right)/2)]
    index = partition(array, left, right, pivot)
    quicksort_implement(array, left, index-1)
    quicksort_implement(array, index, right)


def quicksort(array):
    quicksort_implement(array, 0, len(array)-1)


ar = [random.randint(0,1000) for i in range(100)]
print(ar)
quicksort(ar)
print(ar)

print(1==1==2)