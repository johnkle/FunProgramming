#在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
#每一列都按照从上到下递增的顺序排序。
#请完成一个函数，输入这样的一个二维数组和一个整数，
#判断数组中是否含有该整数。


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        for item in matrix:
            if target in item:
                return True
        return False


class Solution2(object):
    def findNumberIn2DArray(self, matrix, target):
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

sl = Solution2()
matrix = [[1,4,7,11,15],[2,5,8,12,19],\
    [3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(sl.findNumberIn2DArray(matrix,target))