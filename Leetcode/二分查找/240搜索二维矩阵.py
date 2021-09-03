class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return False
        row = 0
        col = len(matrix[0])-1
        while row<=len(matrix)-1 and col>=0:
            num = matrix[row][col]
            if num == target:
                return True
            if num > target:
                col -= 1
            else:
                row += 1
        return False

#看成二叉搜索树，使用DFS，从右上角开始搜索
class Solution2:
    def searchMatrix(self, matrix, target):
        def dfs(row,col):
            if row > len(matrix)-1 or col < 0:
                return False
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                return dfs(row+1,col)
            else:
                return dfs(row,col-1)
        return dfs(0,len(matrix[0])-1)
