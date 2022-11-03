class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = min(strs, key=len)
        min_len = len(min_word)
        i = 0
        while i < len(strs):
            if min_len == 0:
                return ""
            if strs[i][:min_len] != min_word[0:min_len]:
                min_len -= 1
                i = 0
            else:
                i += 1
            
        return strs[0][:min_len]