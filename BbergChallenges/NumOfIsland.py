def numIslands(grid) -> int:
    count = 0
    # j = 0
    # i = 0
    # while True:
    #     if grid[i][j] == '0':
    #         break
    #     if grid[i][j] == '1':
    #         i += 1
    #
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                count += 1
                destroy_land(grid, i,j)
    return count

def is_island(grid, i,j):
    #check edges
    if i == 0:
        if j==0:
            if grid[i+1][j] == '0' and grid[i][j+1] == '0':
                return True
        elif j == len(grid[i])-1:
            if grid[i+1][j] == '0' and grid[i][j-1] == '0':
                return True
        else:
            if grid[i+1][j] == '0' and grid[i][j+1] == '0'and grid[i][j-1] == '0':
                return True
    elif i == len(grid)-1:
        if j == 0:
            if grid[i - 1][j] == '0' and grid[i][j + 1] == '0':
                return True
        elif j == len(grid[i])-1:
            if grid[i - 1][j] == '0' and grid[i][j - 1] == '0':
                return True
        else:
            if grid[i - 1][j] == '0' and grid[i][j + 1] == '0' and grid[i][j - 1] == '0':
                return True
    else:
        if grid[i - 1][j] == '0' and grid[i + 1][j] == '0' and grid[i][j + 1] == '0' and grid[i][j - 1] == '0':
            return True
    return False

def destroy_land(grid, i,j):
    if i < 0 or i==len(grid) or j < 0 or j == len(grid[0]):
        return
    if grid[i][j] == '0':
        return
    grid[i][j] = '0'
    destroy_land(grid, i+1, j)
    destroy_land(grid, i-1, j)
    destroy_land(grid, i,j+1)
    destroy_land(grid, i,j-1)

isd = numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
isa = numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

print(isd, isa)