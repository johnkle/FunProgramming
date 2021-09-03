class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #定义状态和dp
        dp = [[0]*(n) for _ in range(m)]
        dp[0][0] = 1
        #定义base case
        for i in range(1,m):
            if obstacleGrid[i][0]==1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j]==1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        #状态转移
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

class Solution2(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #定义状态和dp
        dp = [[0]*(n+1) for _ in range(m+1)]
        #定义base case
        dp[1][1] = 1 if obstacleGrid[0][0] == 0 else 0
        #状态转移
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m][n]


#dfs+记忆化数组
class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        used = [[0]*col for _ in range(row)]
        def dfs(obstacleGrid, i, j):
            if i < 0 or j < 0 or i > row - 1 or j > col - 1:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == row - 1 and j == col - 1:
                return 1
            # 标记走过的路，下一次不重复走
            if used[i][j]:
                return used[i][j]
            #obstacleGrid[i][j] = 2
            used[i][j] = dfs(obstacleGrid, i, j + 1)+\
                        dfs(obstacleGrid, i + 1, j)
            #obstacleGrid[i][j] = 0
            return used[i][j]
        return dfs(obstacleGrid, 0, 0)