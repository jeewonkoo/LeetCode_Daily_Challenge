class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = [0] * len(words)
        # print(words)
        for i in words: 
            sorted_words[int(i[-1])-1] = i[:-1]
        # print(sorted_words)
        return " ".join(sorted_words)