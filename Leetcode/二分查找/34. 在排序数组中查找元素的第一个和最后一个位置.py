class Solution(object):
    def searchRange(self, nums, target):
        left = self.searchLeft(nums,target)
        right = self.searchRight(nums,target)
        return [left,right]
    def searchLeft(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        if left == len(nums) or nums[left] != target:
            return -1
        return left

    def searchRight(self,nums,target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
        if right < 0 or nums[right]!=target:
            return -1
        return right        



class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left]==target and nums[right]==target:
                return [left,right]
            if nums[left] != target:
                left += 1
            if nums[right] != target:
                right -= 1
        return [-1,-1]