class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, idx):
            if curr not in res: 
                res.append(curr[:])
                
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
            
            
        res = []
        backtrack([], 0)
        return res