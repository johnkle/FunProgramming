class Solution:
    def __init__(self):
        self.count = 1
    def generateMatrix(self, n):
        res = []
        matrix = [[False]*n for _ in range(n)]
        def dfs(matrix,row,col):
            if row<0 or col<0 or row>n-1 or col>n-1 or matrix[row][col]:
                return
            matrix[row][col] = self.count
            self.count += 1
            if col-1<0 or matrix[row][col-1]:
                dfs(matrix,row-1,col)
            dfs(matrix,row,col+1)
            dfs(matrix,row+1,col)
            dfs(matrix,row,col-1)
            dfs(matrix,row-1,col)
        dfs(matrix,0,0)
        return matrix