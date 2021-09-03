class Solution(object):
    def groupAnagrams(self, strs):
        record = dict()
        for item in strs:
            key = ''.join(sorted(item))
            if key not in record:
                record[key] = []
            record[key].append(item)
        return list(record.values())