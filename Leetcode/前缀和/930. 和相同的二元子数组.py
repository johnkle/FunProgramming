class Solution:
    def numSubarraysWithSum(self, nums, goal):
        record = dict()
        record[0] = 1
        pre = 0
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            count += record.get(pre-goal,0)
            if pre not in record:
                record[pre] = 0
            record[pre] += 1
        return count