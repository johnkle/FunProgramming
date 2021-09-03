class Solution(object):
    def rotate(self, matrix):
        left = 0
        right = len(matrix)-1
        while left < right:
            matrix[left],matrix[right] = matrix[right],matrix[left]
            left += 1
            right -= 1
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix

class Solution:
    def rotate(self, matrix):
        matrix.reverse()
        for row in range(len(matrix)):
            for col in range(row,len(matrix[0])):
                matrix [row][col],matrix[col][row] = matrix[col][row],matrix [row][col]
        return matrix

if __name__ =="__main__":
    sl = Solution()
    matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
             ]
    print(sl.rotate(matrix))