class Solution:
    def isValid(self, s):
        pairs = {')':'(',']':'[','}':'{'}
        stack = list()
        for ch in pairs:
            #如果是左括号
            if ch not in pairs:
                stack.append(ch)
            #如果是右括号
            else:
                if not stack or pairs[ch]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack

class Solution:
    def isValid(self, s):
        lookup = {')':'(',']':'[','}':'{'}
        stack = []
        for x in s:
            if x not in lookup:
                stack.append(x)
            else:
                if stack and stack[-1] == lookup[x]:
                    stack.pop()
                else:
                    return False
        return not stack
        
                