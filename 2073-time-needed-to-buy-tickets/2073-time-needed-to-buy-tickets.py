class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        output, back = 0, 0
        
        for i, v in enumerate(tickets): 
            if i > k: back = 1
                
            if v < tickets[k] - back: output += v
                
            else: output += tickets[k] - back
                
        return output 