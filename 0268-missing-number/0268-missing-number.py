class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res, cnt = len(nums), 0
        
        for i in nums:
            res ^= i
            res ^= cnt
            cnt += 1
        
        return res