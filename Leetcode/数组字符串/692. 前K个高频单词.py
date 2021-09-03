import collections
class Solution:
    def topKFrequent(self, words, k):
        record = collections.Counter(words)
        res = sorted(record.items(),key = lambda x:(-x[1],x[0]))
        return [x[0] for x in res][:k]
#如何最小堆实现