#arrange 8 queens on a chess board so that they dont conflict each other
#using brute force, we search every position of a queen for the 8x8 board
#using the normal brute force search, we get time complexity of 64^8
#optimized version... we fix the column for each queen and the search only the row
#this reduces the time complexity to 8^8 possible solutions
#A solution is verified if there is only 1 queen on a row, column and diagonals
#queens lie on same diagonal if delta_row =  delta_col (i.e slope is -1 or 1)


#verify a solution
def verify_solution(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            # check for same row values
            if arr[i] == arr[j]:
               return False
            # check for diagonals
            delta_row = abs(arr[i] - arr[j])
            delta_col = abs(i - j)
            # print(delta_col, delta_row)
            if delta_row == delta_col:
                return False
    return True

count = 0
#optimized solution
for q0r in range(0,8):
    for q1r in range(0, 8):
        for q2r in range(0, 8):
            for q3r in range(0, 8):
                for q4r in range(0, 8):
                    for q5r in range(0, 8):
                        for q6r in range(0, 8):
                            for q7r in range(0, 8):

                                #queen location having its index representing the col nu
                                queen_locations = [q0r,q1r, q2r, q3r, q4r, q5r, q6r, q7r]
                                # print('current', queen_locations)
                                #check if solution is verified
                                if verify_solution(queen_locations):
                                    print('result', queen_locations)
                                    count+=1

print('total ways',count)

