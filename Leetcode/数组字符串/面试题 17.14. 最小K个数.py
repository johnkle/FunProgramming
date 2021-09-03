import heapq
class Solution:
    def smallestK(self, arr, k):
        if not arr or k==0:
            return []
        heap = []
        for x in arr:
            if len(heap) < k:
                heapq.heappush(heap,-x)
            elif -x > heap[0]:
                heapq.heappush(heap,-x)
                heapq.heappop(heap)
        res = []
        while heap:
            t = heapq.heappop(heap)
            res.append(-t)
        res.reverse()
        return res

#一直加，直到>k，pop堆顶元素
class Solution:
    def smallestK(self, arr, k):
        if not arr or k==0:
            return []
        heap = []
        for x in arr:
            heapq.heappush(heap,-x)
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            t = heapq.heappop(heap)
            res.append(-t)
        res.reverse()
        return res