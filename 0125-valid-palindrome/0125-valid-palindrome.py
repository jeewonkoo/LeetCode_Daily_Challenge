class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else: return False
            elif not s[left].isalnum(): left +=1 
                
            elif not s[right].isalnum(): right -=1 
                
                
        return True 