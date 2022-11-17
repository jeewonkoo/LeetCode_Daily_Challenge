class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a_sum, b_sub = sum(aliceSizes), sum(bobSizes)
        
        res = []
        diff = (b_sub - a_sum) / 2
        
        a_set = set(aliceSizes)
        
        for bobItem in bobSizes:
            if bobItem - diff in a_set:
                res.append(int(bobItem - diff))
                res.append(bobItem)
                return res
        return res