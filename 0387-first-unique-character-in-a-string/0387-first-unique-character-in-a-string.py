class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s: 
            d[i] = d.get(i, 0) + 1
        for item in d.items(): 
            if item[1] == 1: return s.index(item[0])
        return -1