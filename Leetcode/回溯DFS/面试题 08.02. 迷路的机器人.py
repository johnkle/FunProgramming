#路径问题优先dfs, 注意减枝
class Solution:
    def pathWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        res = []

        def dfs(obstacleGrid, i, j, path):
            if i < 0 or j < 0 or i > row - 1 or j > col - 1:
                return
            if obstacleGrid[i][j] == 1:
                return
            if obstacleGrid[i][j] == 2:
                return
            # 若找到一条路径，返回，不继续搜索
            if res:
                return
            if i == row - 1 and j == col - 1:
                res.append(path.copy() + [[i, j]])
                return
            # 标记走过的路，下一次不重复走
            obstacleGrid[i][j] = 2
            path.append([i, j])
            dfs(obstacleGrid, i, j + 1, path)
            dfs(obstacleGrid, i + 1, j, path)
            path.pop()
            # obstacleGrid[i][j] = 0

        dfs(obstacleGrid, 0, 0, [])
        return res[0] if res else res

#尝试用动态规划
