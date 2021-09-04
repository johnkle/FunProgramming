import collections
class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 11:
            return []
        left = 0
        right = 9
        record = set()
        res = set()
        while right < len(s):
            substr = s[left:right+1]
            if substr in record:
                res.add(substr)
            else:
                record.add(substr)
            left += 1
            right += 1
        return list(res)

class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 11:
            return []
        record = collections.defaultdict(int)
        left = 0
        right = 9
        res = []
        while right < len(s):
            record[s[left:right+1]] += 1
            left += 1
            right += 1
        for key in record:
            if record[key] > 1:
                res.append(key)
        return res