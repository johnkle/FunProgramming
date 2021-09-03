import re
from typing import Collection
#res = re.fullmatch('\d{3}|','123')
#print(res)
# print(re.match('\(\d{3}\) \d{3}-\d{4}','(123) 456-7890'))
# print(re.fullmatch('\d{3}-\d{3}-\d{4}','987-123-4567'))
#print(re.match('(abc)','abc'))
# print(re.match('(\(\d{3}\) |\d{3}-)\d{3}-\d{4}','987-123-4567'))

class Solution():
    def permute(self,nums):
        res = []
        used = [False]*len(nums)
        self.count = 0
        def dfs(nums,idx,path):
            if idx == len(nums):
                self.count += 1
                # if self.count < 3:
                #     res.append(path.copy())
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                #print('前',path)
                dfs(nums,idx+1,path)
                if self.count >= 3:
                    break
                path.pop()
                #print('后',path)
                used[i] = False

        dfs(nums,0,[])
        return res

lst = [3,2,5]

import re
s = ' bacbbccb'
s1 = re.sub('b{2,2}','f',s)

import math
import collections
print(math.floor(pow(6,0.5)))
print(collections.Counter('abb'))

