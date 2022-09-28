class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target in nums: return nums.index(target)
        # for i,v in enumerate(nums):
        #     if v > target: return i
        # return len(nums)
        
        #O(log n)
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < target: l = mid +1
            else: r = mid 
        return l