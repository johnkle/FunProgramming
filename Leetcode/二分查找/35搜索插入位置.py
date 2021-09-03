class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left

class Solution2:
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            if nums[mid] < target:
                left = mid+1
        return left

class Solution3(object):
    def searchInsert(self, nums, target):
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target < nums[i+1]:
                return i+1