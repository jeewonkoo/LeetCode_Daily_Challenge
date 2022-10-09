class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output, i = 0, 0
        while i < len(nums)-1:
            output += min(nums[i], nums[i+1])
            i += 2
        return output