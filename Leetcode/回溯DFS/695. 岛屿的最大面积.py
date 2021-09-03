#注意dfs有返回值和无返回值的区别
class Solution:
    def maxAreaOfIsland(self, grid):
        row = len(grid)
        col = len(grid[0])
        res = 0
        def dfs(grid,m,n,level,path):
            if m<0 or n<0 or m>row-1 or n>col-1 or grid[m][n] != 1:
                return
            grid[m][n] = "#"
            path.append(1)
            dfs(grid,m,n+1,level+1,path)
            dfs(grid,m+1,n,level+1,path)
            dfs(grid,m,n-1,level+1,path)
            dfs(grid,m-1,n,level+1,path)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    #记录每个岛屿的路径, path是整个dfs路径
                    path = []
                    dfs(grid,i,j,0,path)
                    res = max(res,sum(path))
        return res

class Solution:
    def maxAreaOfIsland(self, grid):
        row = len(grid)
        col = len(grid[0])
        res = 0
        def dfs(grid,m,n,level):
            if m<0 or n<0 or m>row-1 or n>col-1 or grid[m][n] != 1:
                return 0
            grid[m][n] = "#"
            return 1 +\
                   + dfs(grid,m,n+1,level+1)\
                   + dfs(grid,m+1,n,level+1)\
                   + dfs(grid,m,n-1,level+1)\
                   + dfs(grid,m-1,n,level+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res,dfs(grid,i,j,0))
        return res