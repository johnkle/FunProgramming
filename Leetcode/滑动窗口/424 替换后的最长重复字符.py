#找到最长子串 使得子串最多数的元素的次数至少为len(window)-k 非多数字符数量不超过k
import collections
class Solution:
    def characterReplacement(self, s, k):
        left = 0
        right = 0
        window = collections.Counter()
        res = 0
        while right < len(s):
            c = s[right]
            window[c] += 1
            key, value = window.most_common(1)[1]
            while right-left+1-value > k: #若窗口非多数字符不满足条件
                window[s[left]] -= 1
                if s[left] == key: #更新窗口内最多数字符
                    value -= 1
                left += 1
            res += 1
            right += 1
        return res


