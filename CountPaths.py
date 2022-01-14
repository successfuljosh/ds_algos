#count path from the top to the bottom of a grid with some paths blocked by 'B'

#has time complex as O(2^n^2) and space compex as O(n^2)
def count_paths(grid, row, col):
    #check for invalid boxez
    if row<0 or col<0 or row==len(grid) or col==len(grid[0]):
        return 0

    #at the end
    if row==len(grid)-1 and col==len(grid[0])-1:
        return 1
    #condition
    if grid[row][col] == 'B': return 0
    return count_paths(grid, row+1, col) + count_paths(grid, row, col+1)

#optimizing using memoization
#has both space and runtime as O(n^2)
dic_mem={}
def count_path_mem(grid, row, col):
    if (row,col) in dic_mem:
        return dic_mem[(row, col)]
    #check for invalid boxez
    if row<0 or col<0 or row==len(grid) or col==len(grid[0]):
        return 0
    #at the end
    if row==len(grid)-1 and col==len(grid[0])-1:
        return 1
    if grid[row][col] == 'B': return 0

    dic_mem[(row,col)] = count_path_mem(grid, row+1, col) + count_path_mem(grid, row, col+1)
    return dic_mem[(row,col)]


n=3
box = [[0 for j in range(n)] for i in range(n)]
box[1][1] = 'B'
print(box)
paths = count_paths(box, 0, 0)
# paths = count_path_mem(box, 0, 0)
print(paths)