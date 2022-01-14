#receive from user
# N,M = input().split(' ')
# N,M  = int(N), int(M)
# country=[]
# for i in range(N):
#     Va = input().split(' ')
#     arr = [int(a) for a in Va]
#     country.append(arr)

country = [[1,1,1],
           [4,3,2],
           [3,3,2]]
# country = [[1,2,1],
#            [1,1,1],
#            [1,3,1]]
N=3
M=3
#
N=M=2
country = [[1,1],
           [1,1]]


# def is_rectangle(array,x,y):
#    if y+1==len(array[x]) and x+1==len(array):
#            return True
#
#    if y+1==len(array[x]) and x<len(array):
#        if array[x][y] == array[x + 1][y]:
#            return True
#
#    if x + 1 == len(array) and y < len(array[x]):
#        if array[x][y]==array[x][y+1]:
#            return True
#
#    if array[x][y]==array[x+1][y]==array[x][y+1]==array[x+1][y+1]:
#        return True
#
#    return False


def is_rectangle(array,x,y,a,b):
   if b==len(array[x]) and a==len(array):
           return True

   if b==len(array[x]) and x<len(array):
       if array[x][y] == array[a][y]:
           return True

   if a == len(array) and y < len(array[x]):
       if array[x][y]==array[x][b]:
           return True

   if array[x][y]==array[a][y]==array[x][b]==array[a][b]:
       return True

   return False

# visited={}
# for i in range(N):
#     for j in range(M):
#         identifier = country[i][j]
#         if identifier not in visited:
#             index_list =[(i,j)]
#             visited[identifier] = index_list, 0
#         else:
#             index_list,count = visited[identifier]
#             for (a,b) in index_list:
#                 # if i!=a and j!=b and (i==a+1 or j==b+1):
#                 if not is_rectangle(country,i,j,a,b):
#                     count += 1
#             index_list.append((i,j))
#             visited[identifier] = index_list, count
#

#IDENTIFY COUNTRIES WITH THEIR POSITION
countries={}
for i in range(N):
    for j in range(M):
        region = country[i][j]
        if region not in countries:
            index_list =[(i,j)]
            countries[region] = index_list, 0
        else:
            index_list,count = countries[region]
            index_list.append((i,j))
            countries[region] = index_list,count

#CHECK FOR NON RECTANGLES
def non_rectangle(coord):
    #check rows
    for i in range(len(coord)):
        for j in range(i+1,len(coord)):
            if coord[i][0]==coord[j][0] and coord[j][1]-coord[i][1] > 1:
                return True
    # check columns
    for i in range(len(coord)):
        for j in range(i + 1, len(coord)):
            if coord[i][1] == coord[j][1] and coord[i][0] - coord[j][0] > 1:
                return True
    return False

for k,v in countries.items():
    index_list, count = v
    if non_rectangle(index_list):
        count += 1
    countries[k] = index_list, count

total = 0
for _,count in countries.values():
    total+=count

print(countries)
print('total non rectangular is', total)
print(total)


# def count_non_rectangles(arr,i,j):
#     if i<0 or j<0 or i==len(arr) or j==len(arr):
#         return 0
#     #check for end
#     if i==len(arr)-1 and j==len(arr[0])-1:
#         return 0
#     # parentA = arr[i-1][j]
#     # parentB = arr[i][j-1]
#     if count_non_rectangles(arr, i + 1, j) != arr[i][j] or count_non_rectangles(arr, i, j + 1) != arr[i][j]:
#         return 1
#     return 0
#     # if count_non_rectangles(arr, i + 1, j) == count_non_rectangles(arr, i, j + 1):
#     #     return 1
#     # return count_non_rectangles(arr, i + 1, j) + count_non_rectangles(arr, i, j + 1)
# #
# country = [[1,1],
#            [1,1]]
# print(count_non_rectangles(country, 0, 0))