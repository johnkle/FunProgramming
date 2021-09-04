"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""
import collections
class Solution:
    def minWindow(self, s, t):
        left = 0
        right = 0
        window = collections.defaultdict(int)
        record = collections.Counter(t)
        count = 0
        res = ''
        while right < len(s):
            c = s[right]
            window[c] += 1
            if window[c] <= record[c]:
                count += 1
            while left < len(s) and window[s[left]] > record.get(s[left],0):
                window[s[left]] -= 1
                left += 1
            if count == len(t):
                if not res or right-left+1<len(res):
                    res = s[left:right+1]
            right += 1
        return res

#每次都向窗口中加入元素 直到窗口满足条件 从左收缩窗口
class Solution:
    def minWindow(self, s, t):
        left = 0
        right = 0
        window = collections.defaultdict(int)
        record = collections.Counter(t)
        #计数器 窗口中必需元素的个数
        count = 0
        res = ''
        while right < len(s):
            c = s[right]
            window[c] += 1
            #加入t所必须的元素
            if window[c] <= record[c]:
                #若是必需元素，计数器+1
                count += 1
            #若窗口元素满足条件，即覆盖t所有字符，从左边收缩窗口
            while count == len(t):
                #先更新res
                if not res or right-left+1<len(res):
                    res = s[left:right+1]
                window[s[left]] -= 1
                #收缩了必需元素，计数器-1
                if window[s[left]] < record[s[left]]:
                    count -= 1
                left += 1
            #继续向右拓展窗口
            right += 1
        return res

#set不重复！！用dict
if __name__ == "__main__":
    sl = Solution()
    s = "a"
    t = "aa"
    print(sl.minWindow(s,t))                     
