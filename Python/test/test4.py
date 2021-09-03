class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        heights = [0 for _ in range(n)]
        area = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            area = max(area, self.helper(heights))
        return area

    # def helper(self, height):
    #     res = 0
    #     for i in range(len(height)):
    #         for j in range(i, len(height)):
    #             area = min(height[i:j + 1]) * (j - i + 1)
    #             res = max(res, area)
    #     return res

    #84单调栈
    def helper(self,heights):
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res

if __name__ == "__main__":
    sl = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], \
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(sl.maximalRectangle(matrix))
