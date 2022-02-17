#what is the time complexity to sort an array of string also sorting each string?
#we using quicksort having O(nlogn)
#let s = len of longest string
# let a len of array
#we sort each string => O(slogs)
#there are a strings => O(aslogs)
#We sort the array => O(aloga)
#for each sort, there are s string len = O(asloga)
#total complexity => O(aslogs + asloga) ==> O( as(logs + loga))

#implementation
def quick_sort_string(s):
    if len(s) < 2: return s
    left = ''
    right = ''
    for i in range(1, len(s)):
        if s[i] >= s[0]:
            right += s[i]
        else:
            left += s[i]
    return quick_sort_string(left) + s[0] + quick_sort_string(right)

def string_a_greater_or_equal_to_string_b(str_a, str_b):
    longeer_string = lambda x,y: x if(len(x) >= len(y)) else y, str_a, str_b
    for i in range(len(longeer_string)):
        if not str_a[i]: return False
        if not str_b[i]: return True
        if str_a[i] >= str_b[i]: return True
        if str_a[i] < str_b[i]: return False



def quick_array_sort(arr):
    if len(arr) < 2: return arr

    left_arr=[]
    right_arr=[]
    for i in range(1, len(arr)):
        if arr[i] >= arr[0]:      #string_a_greater_or_equal_to_string_b(arr[i],arr[0]):
            right_arr.append(arr[i])
        else:
            left_arr.append(arr[i])
    return quick_array_sort(left_arr) + [arr[0]] + quick_array_sort(right_arr)

def sort_arr_str(lists_str):
    new_arr = []
    for i in lists_str:
        sorted_string = quick_sort_string(i)
        new_arr.append(sorted_string)
    return quick_array_sort(new_arr)

print(quick_sort_string('sadeisgrdse'))
ar_test = ['sas2','3w1','aq3','3','2']
print(quick_array_sort(ar_test))
print(sort_arr_str(ar_test))