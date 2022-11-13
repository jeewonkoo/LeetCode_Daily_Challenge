class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        largest = -1
        for k,v in d.items():
            if k == v :
                largest = max(v, largest)
        return largest