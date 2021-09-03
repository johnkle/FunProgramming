import collections
class Solution:
    def topKFrequent(self, nums, k):
        lookup = collections.Counter(nums)
        return sorted(lookup,key = lookup.__getitem__,reverse=True)[:k]

class Solution2:
    def topKFrequent(self, nums, k):
        lookup = collections.Counter(nums)
        return list(map(lambda x:x[0],lookup.most_common(k)))
