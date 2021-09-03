class Solution(object):
    def rotate(self, nums, k):
        for _ in range(k):
            temp = nums.pop(-1)
            nums.insert(0,temp)
        return nums
sl = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(sl.rotate(nums,k))