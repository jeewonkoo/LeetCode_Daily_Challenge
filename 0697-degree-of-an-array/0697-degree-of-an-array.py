class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
        m = max([ len(v) for v in d.values() ])
        res = len(nums)
        for v in d.values():
            if len(v)==m: res = min(res,v[-1]-v[0]+1)
        return res