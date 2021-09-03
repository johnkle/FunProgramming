class Solution:
    def findMinDifference(self, timePoints):
        for i in range(len(timePoints)):
            timePoints[i] = int(timePoints[i][:2])*60 + int(timePoints[i][3:])
        timePoints.sort()
        dp = [float('inf')]*len(timePoints)
        dp[0] = 0
        for i in range(1,len(dp)):
            dp[i] = min(timePoints[i]-timePoints[i-1],\
                        24*60-timePoints[i]+timePoints[0])
        return min(dp[1:])
