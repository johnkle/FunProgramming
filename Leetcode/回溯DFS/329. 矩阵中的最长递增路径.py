# 先判断下一步是否符合条件，进行下一步搜索
class Solution:
    def longestIncreasingPath(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 1
        memo = [[0] * cols for _ in range(rows)]

        def dfs(matrix, m, n):
            if memo[m][n]:
                return memo[m][n]
            # 注意此句的含义
            memo[m][n] += 1
            for x, y in dirs:
                if m + x >= 0 and n + y >= 0 and m + x < rows and n + y < cols \
                        and matrix[m][n] < matrix[m + x][n + y]:
                    memo[m][n] = max(memo[m][n], dfs(matrix, m + x, n + y) + 1)
            return memo[m][n]

        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(matrix, i, j))
        return res
