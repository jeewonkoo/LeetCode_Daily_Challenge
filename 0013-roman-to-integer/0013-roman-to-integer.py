class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"M":1000, "D":500, "C":100, "L":50, "X":10,"V":5, "I":1}
        res = 0
        i=0
        if(len(s) == 2):
            if roman[s[0]] < roman[s[1]]:
                res += roman[s[1]] - roman[s[0]] 
            else:
                for i in range(2):
                    res+=roman[s[i]]
        else :
            while i < len(s)-1:
                if roman[s[i]] < roman[s[i+1]]:
                    res += roman[s[i+1]] - roman[s[i]]
                    i+=1
                else: 
                    res += roman[s[i]]
                i+=1
            if(len(s) != 2): #last letter 
                if roman[s[len(s)-2]] >= roman[s[len(s)-1]]:
                    res += roman[s[len(s)-1]]

        
        return res