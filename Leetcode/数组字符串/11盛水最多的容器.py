#每次移动较小指针边界
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        res = 0
        while left != right:
            wide = right-left
            if height[left] < height[right]:
                high = height[left]
                left += 1
            else:
                high = height[right]
                right -= 1
            res = max(res,wide*high)
        return res

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            area = min(height[left],height[right])*(right-left)
            res = max(res,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res