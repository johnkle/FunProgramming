class Solution:
    def isAdditiveNumber(self, num):
        res = []
        def dfs(num,begin,path):
            if begin==len(num) and len(path)>=3:
                res.append(path.copy())
                return
            for i in range(begin,len(num)):
                #判断什么条件下将选择加入path
                if len(num[begin:i+1])>1 and num[begin]=='0':
                    continue
                if len(path)<2:
                    path.append(int(num[begin:i+1]))
                elif int(num[begin:i+1]) == path[-1]+path[-2]:
                    path.append(int(num[begin:i+1]))
                else:
                    continue
                dfs(num,i+1,path)
                path.pop()
            #res非空表示获得一个合法的path，回溯结束，返回
            return res!=[]
        return dfs(num,0,[])