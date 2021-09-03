class Solution:
    def numberOfArithmeticSlices(self, nums):
        count = 0
        for i in range(1,len(nums)):
            d = nums[i]-nums[i-1]
            for j in range(i+1,len(nums)):
                if nums[j]-nums[j-1] == d:
                    count += 1
                else:
                    break
        return count

#dp[i] 以nums[i]结尾的等差数列的数目，看nums[i]能否接在nums[i-1]后面
class Solution:
    def numberOfArithmeticSlices(self, nums):
        dp = [0 for _ in range(len(nums))]
        for i in range(2,len(dp)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1
        return sum(dp)