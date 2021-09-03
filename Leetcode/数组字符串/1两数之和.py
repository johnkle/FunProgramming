class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left,right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return 

if __name__ == "__main__":
    sl = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sl.twoSum(nums,target))