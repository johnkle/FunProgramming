class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left+(right-left)//2
            #去重
            if nums[right] == nums[mid]:
                right -= 1
            #每次都在无序区间查找
            elif nums[mid]<nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]