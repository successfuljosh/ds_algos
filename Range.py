#search for consecutive smallest
import sys

def consecutive_smallest(arr):
    temp = arr.copy()
    temp_a = arr.copy()
    conse_dict={}
    while temp!=[]:
        small = min(temp_a)
        small_index = temp_a.index(small)
        if conse_dict == {}:
            conse_dict[small_index] = small
            temp.pop(small_index)
            temp_a[small_index] = sys.maxsize
        else:
            indexes = list(conse_dict.keys())
            #check if it contains small index
            if small_index in indexes:
                continue
            #check if the last smallest is close to the current smallest (consecutive)
            if indexes[-1] == small_index + 1 or indexes[-1] == small_index - 1:
                conse_dict[small_index] = small
                temp.pop(small_index)
                temp_a[small_index] = sys.maxsize
            else:
                break

    return conse_dict


def range(main_arr, N):
    mar_turn = True
    mar_scores = 0
    zen_scores = 0

    while main_arr != []:
        con = consecutive_smallest(main_arr)
        print(con)
        scores = 0
        for i,x in con.items():
            scores += N**x
            main_arr.pop(i)
        if mar_turn:
            mar_scores += scores
        else:
            zen_scores += scores
        mar_turn = not mar_turn

    if mar_scores < zen_scores:
        print('Marichka')
    elif mar_scores > zen_scores:
        print('Zen')
    else:
        print('Draw')

arr = [4,4,7,1]
N = 4
# print(range(arr,N))

arr=[2,1,9,3,7,9,6,1,9,8]
#2 stones to the left of 9 [1,2]
#2 stones to the right of 9
#2 stones to the left of 9
#1 stone to the right of 9
print(consecutive_smallest(arr))