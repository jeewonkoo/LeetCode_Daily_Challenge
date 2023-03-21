class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d: return True
            d[i] = d.get(i, 0) + 1
        return False