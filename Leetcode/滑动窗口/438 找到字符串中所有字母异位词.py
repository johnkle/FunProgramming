import collections
class Solution:
    def findAnagrams(self, s, p):
        left = 0
        right = 0
        res = []
        window = [0]*26
        pcount = [0]*26
        for x in p:
            pcount[ord(x)-ord('a')] += 1
        while right < len(s):
            c = ord(s[right])-ord('a')
            window[c] += 1
            while window[c] > pcount[c]:
                window[ord(s[left])-ord('a')] -= 1
                left += 1
            if window == pcount:
                res.append(left)
            right += 1
        return res

#每次都向窗口中加入必需词 若不是必需词 从左收缩窗口 直到窗口元素满足条件
class Solution2:
    def findAnagrams(self, s, p):
        window = collections.defaultdict(int)
        #构成p的异位词的必需词字典
        record = collections.Counter(p)
        #计数器 窗口中必需词的个数
        count = 0
        left = 0
        right = 0
        res = []
        while right < len(s):
            c = s[right]
            window[c] += 1
            #若是必需词 计数器+1
            if window[c] <= record[c]:
                count += 1
            #若窗口不满足条件 即窗口词数量>必需词数量 从左收缩
            while window[c] > record[c]:
                window[s[left]] -= 1
                #若收缩了必需元素 计数器-1
                if window[s[left]] < record[s[left]]:
                    count -= 1
                left += 1
            #若窗口必需词数量==必需词数量 更新res
            if count == len(p):
                res.append(left)
            right += 1
        return res