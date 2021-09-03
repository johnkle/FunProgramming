#贪心 按区间结尾排序,每次选择区间结尾最早的且和前一个区间不重叠的区间
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        right = intervals[0][1]
        res = 1
        for i in range(1,len(intervals)):
            if intervals[i][0] >= right:
                res += 1
                right = intervals[i][1]
        return len(intervals)-res

#dp超时
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        dp = [1]*len(intervals)
        for i in range(1,len(dp)):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return len(intervals)-max(dp)