# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r: 
            m = (l+r) // 2
            if not isBadVersion(m-1) and isBadVersion(m): return m
            if isBadVersion(m): r = m - 1
            else: l = m + 1
        return m