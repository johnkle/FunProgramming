class Solution:
    def restoreIpAddresses(self, s):
        res = []
        def dfs(s,begin,path):
            #终止条件
            if len(path) == 4 and begin==len(s):
                res.append('.'.join(path.copy()))
                return
            if len(path) > 4:
                return
            #选择划分点
            for i in range(begin,len(s)):
                if not check(s[begin:i+1]):
                    continue
                if len(s[i+1:])>10:
                    continue
                #每次加入一个合法的ip段
                path.append(s[begin:i+1])
                dfs(s,i+1,path)
                path.pop()
        #检查加入path的ip段是否合法
        def check(s):
            if s == '0':
                return True
            elif 1<=int(s)<=255 and not s.startswith('0'):
                return True
            return False
        dfs(s,0,[])
        return res