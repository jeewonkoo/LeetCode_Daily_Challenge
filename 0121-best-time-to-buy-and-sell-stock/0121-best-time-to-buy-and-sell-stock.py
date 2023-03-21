class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min, curr_profit = float('inf'), 0
        max_profit = 0
        
        for i in prices:
            if i < curr_min: 
                curr_min = i
            curr_profit = i - curr_min
            max_profit = max(max_profit, curr_profit)
            
        return max_profit