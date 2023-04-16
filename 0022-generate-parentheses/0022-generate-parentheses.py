class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(opened, closed, curr_str, res):
            if len(curr_str) == 2*n:
                res.append(curr_str)
                return 
            if closed < opened:
                if opened < n: backtrack(opened+1, closed, curr_str+"(", res)
                if opened > 0: backtrack(opened, closed+1, curr_str+")", res)
                
            elif closed == opened:
                backtrack(opened+1, closed, curr_str+"(", res)
                backtrack(opened, closed+1, curr_str+")", res)
                
        res = []
        backtrack(0, 0, "", res)
        return res