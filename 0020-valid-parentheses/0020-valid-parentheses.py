class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{":"}", "[":"]"}
        stack = []
        for i in s:
            if i in d.keys():
                stack.append(i)
            elif i in d.values():
                if not stack: return False 
                if d[stack[-1]] == i:
                    stack.pop()
                else: return False
        
        return len(stack) == 0