class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0 
        
        left = 0 
        counter = 0
        seen = set()
        
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            counter = max(counter, i - left + 1)
            
        return counter 