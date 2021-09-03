#生成所有长度等于len(digits)的字母组合
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup = {'2':'abc',
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        res = []
        def dfs(digits,begin,path):
            if begin == len(digits):
                res.append(''.join(path.copy()))
                return
            num = digits[begin]
            letters = lookup[num]
            for c in letters:
                path.append(c)
                dfs(digits,begin+1,path)
                path.pop()
        dfs(digits,0,[])
        return res

#生成所有长度小于等于len(digits)的字母组合
class Solution2:
    def letterCombinations(self, digits):
        if not digits:
            return []
        phoneDict = {'2':'abc',
                    '3':'def',
                    '4':'ghi',
                    '5':'jkl',
                    '6':'mno',
                    '7':'pqrs',
                    '8':'tuv',
                    '9':'wxyz'}
        res = []
        def dfs(digits,idx,path):
            if idx <= len(digits):
                res.append(''.join(path))
                if idx == len(digits):
                    return
            for i in range(idx,len(digits)):
                num = digits[i]
                letters = phoneDict[num]
                for x in letters:
                    path.append(x)
                    print('前',path)
                    dfs(digits,i+1,path)
                    path.pop()
                    print('后',path)
        dfs(digits,0,[])
        return res

sl = Solution2()
digits = '23'
res = sl.letterCombinations(digits)
print(res)