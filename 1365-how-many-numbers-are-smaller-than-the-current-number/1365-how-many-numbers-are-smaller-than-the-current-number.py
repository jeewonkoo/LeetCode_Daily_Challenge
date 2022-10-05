class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_ = sorted(nums)
        return(sorted_.index(a) for a in nums)