# 找到数组的中间元素 mid。
# 如果中间元素 > 数组第一个元素，我们需要在 mid 右边搜索变化点
# 如果中间元素 < 数组第一个元素，我们需要在 mid 左边搜索变化点。
class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        if nums[0] < nums[right]:
            return nums[0]
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[left] < nums[mid]:
                left = mid+1
            else:
                right = mid-1

#每次都找到有序数组的第一个元素，并且在更新搜索区间
class Solution2(object):
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        ans = float('inf')
        while left <= right:
            mid = left+(right-left)//2
            if nums[left]<=nums[mid]:
                if nums[left] < ans:
                    ans = nums[left]
                left = mid+1
            else:
                if nums[mid] < ans:
                    ans = nums[mid]
                right = mid-1
        return ans

class Solution3:
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left+(right-left)//2
            #每次都在无序区间查找
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]
        