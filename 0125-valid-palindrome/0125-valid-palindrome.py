class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s: 
            if i.isalpha() or i.isnumeric(): string += i.lower()
        return string == string [::-1] 