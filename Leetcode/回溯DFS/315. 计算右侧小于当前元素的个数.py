class Solution():
    def countSmaller(self, nums):
        res = []
        target = 6
        def dfs(nums,pos,idx,path):
            if pos == len(nums):
                res.append(path.copy())
                return
            for i in range(pos,len(nums)):
                if nums[i] >= target:
                    continue
                path.append(nums[i])
                print('前',path)
                dfs(nums,i+1,idx+1,path)
                path.pop()
                print('后',path)       
        dfs(nums,0,0,[])
        return res

sl = Solution()
nums = [7,1,6,5,9,2,3]
res = sl.countSmaller(nums)
print(res)