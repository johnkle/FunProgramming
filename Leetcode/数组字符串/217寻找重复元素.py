class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for x in nums:
            if x in lookup:
                return True
            lookup.add(x)
        return False