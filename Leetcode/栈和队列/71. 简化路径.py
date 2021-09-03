class Solution:
    def simplifyPath(self, path):
        stack = []
        temp = path.split('/')
        for x in temp:
            if x not in ['.','..',''] :
                stack.append(x)
            if x == '..' and stack:
                stack.pop()
        return f"/{'/'.join(stack)}"