import collections
class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        left = 0
        right = 0
        record = collections.Counter(s1)
        window = collections.defaultdict(int)
        count = 0
        while right < len(s2):
            c = s2[right]
            window[c] += 1
            if window[c] <= record[c]:
                count += 1
            while window[c] > record[c]:
                window[s2[left]] -= 1
                if window[s2[left]] < record[s2[left]]:
                    count -= 1
                left += 1
            if count == len(s1):
                return True
            right += 1
        return False