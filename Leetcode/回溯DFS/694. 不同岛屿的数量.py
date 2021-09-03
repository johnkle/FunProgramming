class Solution:
    def numDistinctIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        res = []
        def dfs(grid,m,n,i,j,level,path):
            if m<0 or n<0 or m>row-1 or n>col-1 or grid[m][n] != 1:
                return
            #记录相对路径
            path.append((m-i,n-j))
            grid[m][n] = "#"
            dfs(grid,m,n+1,i,j,level+1,path)
            dfs(grid,m+1,n,i,j,level+1,path)
            dfs(grid,m,n-1,i,j,level+1,path)
            dfs(grid,m-1,n,i,j,level+1,path)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    #对每个岛屿, 记录整个dfs相对路径
                    path = []
                    dfs(grid,i,j,i,j,0,path)
                    if path not in res:
                        res.append(path)
        return len(res)