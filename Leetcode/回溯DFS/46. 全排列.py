class Solution():
    def permute(self,nums):
        res = []
        used = [0 for _ in range(len(nums))]
        def dfs(nums,level,path):
            if level == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                dfs(nums,level+1,path)
                path.pop()
                used[i] = 0
        dfs(nums,0,[])
        return res


class Solution3:
    def permute(self, nums):
        if not nums: return []
        res = []
        used = [0] * len(nums)
        def backtrack(nums, path, used):
            # 终止条件
            if len(nums) == len(path):
                res.append(path.copy())
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums, path, used)
                path.pop()
                used[i] = 0
        # 别忘了排序
        backtrack(sorted(nums), [], used)
        return res

if __name__ == "__main__":
    sl = Solution()
    nums = [1,2,3]
    print(sl.permute(nums))
