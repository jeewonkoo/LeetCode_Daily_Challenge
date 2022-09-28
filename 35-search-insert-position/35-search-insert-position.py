class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: return nums.index(target)
        for i,v in enumerate(nums):
            if v > target: return i
        return len(nums)