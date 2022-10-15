class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_, t_ = [], []
        
        for i in s:
            if i == "#" and s_:
                s_.pop()
            elif i != "#": s_.append(i)
            
        for i in t:
            if i == "#" and t_:
                t_.pop()
            elif i != "#": t_.append(i)
        
        # print(s_, t_)
        return s_ == t_