#岛屿的周长就是岛屿方格和非岛屿方格相邻的边的数量，即dfs超越边界的次数
class Solution:
    def __init__(self):
        self.count = 0

    def islandPerimeter(self, grid):
        row = len(grid)
        col = len(grid[0])

        def dfs(grid, m, n, level):
            if m < 0 or n < 0 or m > row - 1 or n > col - 1 or grid[m][n] == 0:
                # 超越边界的次数
                self.count += 1
                return
            if grid[m][n] == 2:
                return
            grid[m][n] = 2
            dfs(grid, m, n + 1, level + 1)
            dfs(grid, m + 1, n, level + 1)
            dfs(grid, m, n - 1, level + 1)
            dfs(grid, m - 1, n, level + 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(grid, i, j, 0)
        return self.count

class Solution:
    def islandPerimeter(self, grid):
        row = len(grid)
        col = len(grid[0])
        #从[m,n]开始搜索得到的周长
        def dfs(grid,m,n,level):
            if m<0 or n<0 or m>row-1 or n>col-1 or grid[m][n]==0:
                #如果超越边界，得到一个周长
                return 1
            if grid[m][n] == 2:
                return 0
            grid[m][n] = 2
            return  dfs(grid,m,n+1,level+1)+\
                    dfs(grid,m+1,n,level+1)+\
                    dfs(grid,m,n-1,level+1)+\
                    dfs(grid,m-1,n,level+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(grid,i,j,0)
