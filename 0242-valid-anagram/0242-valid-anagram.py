class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def createDictionary(string):
            dic = {}
            for i in string:
                dic[i] = dic.get(i, 0) + 1
            return dic 
        
        s_dic = createDictionary(s)
        t_dic = createDictionary(t)
        
        return s_dic == t_dic