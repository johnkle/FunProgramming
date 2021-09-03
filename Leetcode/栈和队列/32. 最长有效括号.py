class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if not stack or stack[-1]==-1 or s[i]=='(':
                stack.append(i)
            if s[i] == ')':
                if s[stack[-1]] == '(':
                    stack.pop()
                    res = max(res,i-stack[-1])
                else:
                    stack.append(i)
        return res

#dp[i] 以i结尾的字符串最长有效括号的长度
class Solution(object):
    def longestValidParentheses(self, s):
        maxLen = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1,len(s)):
            if s[i]==')' and s[i-1]=='(':
                dp[i] = dp[i-2]+2 if i-2>=0 else 2
            elif s[i]==')' and s[i-1]==')' and s[i-dp[i-1]-1]=='(' and i-dp[i-1]>0:
                if i-dp[i-1]-2>=0:
                    dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                else:
                    dp[i] = dp[i-1]+2
            maxLen = max(maxLen,dp[i])
        return maxLen

class Solution(object):
    def longestValidParentheses(self, s):
        maxLen = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1,len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i] = dp[i-2]+2 if i-2>=0 else 2
                elif s[i-dp[i-1]-1]=='(' and i-dp[i-1]-1>=0:
                    if i-dp[i-1]-2>=0:
                        dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                    else:
                        dp[i] = dp[i-1]+2
            maxLen = max(maxLen,dp[i])
        return maxLen
