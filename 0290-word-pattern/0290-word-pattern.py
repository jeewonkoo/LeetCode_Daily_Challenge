class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(word) != len(pattern): return False
        
        for i in range(len(word)):
            if pattern.find(pattern[i]) != word.index(word[i]): return False
        return True