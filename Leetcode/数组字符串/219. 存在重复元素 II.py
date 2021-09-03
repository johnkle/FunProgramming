class Solution:
    def containsNearbyDuplicate(self, nums, k):
        record = dict()
        for i in range(len(nums)):
            if nums[i] in record:
                if i-record[nums[i]]<=k:
                    return True
            record[nums[i]] = i
        return False