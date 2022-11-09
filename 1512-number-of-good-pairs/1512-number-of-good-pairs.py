class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                res += dic[n]
                dic[n] +=1
        
        return res