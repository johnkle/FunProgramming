# https://leetcode-cn.com/problems/spiral-matrix/solution/shen-du-you-xian-sou-suo-dfs-by-xiaolei5-a9ko/
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return
        res = []
        row = len(matrix)
        col = len(matrix[0])
        visited = [[False]*col for _ in range(row)]
        def dfs(matrix,m,n):
            if m<0 or n<0 or m>row-1 or n>col-1 or visited[m][n]:
                return
            res.append(matrix[m][n])
            visited[m][n] = True
            #很关键 注意左边，必须优先是往上跑
            if n-1<0  or visited[m][n-1]:
                dfs(matrix,m-1,n)
            dfs(matrix,m,n+1)
            dfs(matrix,m+1,n)
            dfs(matrix,m,n-1)
            dfs(matrix,m-1,n)
        dfs(matrix,0,0)
        return res

if __name__ == "__main__":
    pass