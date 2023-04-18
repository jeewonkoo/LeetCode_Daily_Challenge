class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n == h: return max(piles)
        
        l, r = 1, max(piles)
        temp = 0
        k = float('inf')
        while l <= r:
            temp = 0
            mid = (l+r) // 2
            for pile in piles:
                temp += math.ceil(pile/mid)
            # print(temp)
            if temp > h:
                l = mid + 1
            else:
                r = mid - 1 
                k = min(k, mid)
            
            # print(mid)
                
        return k