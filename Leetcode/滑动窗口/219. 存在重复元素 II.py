class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        record = set()
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] in record:
                return True
            record.add(nums[right])
            while len(record)>k:
                record.discard(nums[left])
                left = left+1
            right += 1
        return False

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        record = dict()
        for i in range(len(nums)):
            if nums[i] in record:
                if i-record[nums[i]]<=k:
                    return True
            record[nums[i]] = i
        return False