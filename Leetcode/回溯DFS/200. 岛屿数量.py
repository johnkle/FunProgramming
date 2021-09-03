#每遇到'1'就进行dfs, 并将'1'标记为已访问, dfs次数即为岛屿数量
class Solution:
    def __init__(self):
        self.count = 0
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        def dfs(grid,m,n,level):
            if m<0 or n<0 or m>row-1 or n>col-1 or grid[m][n] != "1":
                return
            grid[m][n] = "#"
            dfs(grid,m,n+1,level+1)
            dfs(grid,m+1,n,level+1)
            dfs(grid,m,n-1,level+1)
            dfs(grid,m-1,n,level+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(grid,i,j,0)
                    self.count += 1
        return self.count