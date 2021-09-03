import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        for a in nums1:
            for b in nums2:
                if len(heap) < k:
                    heapq.heappush(heap,[-a-b,a,b])
                elif -a-b > heap[0][0]:
                    heapq.heappush(heap,[-a-b,a,b])
                    heapq.heappop(heap)
                else:
                    break
        res = []
        while heap:
            t = heapq.heappop(heap)
            res.append([t[1],t[2]])
        return list(reversed(res))
