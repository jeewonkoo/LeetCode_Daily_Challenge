class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                m = len(nums) // 2
                l, r = nums[:m], nums[m:]
        
                mergeSort(l)
                mergeSort(r)

                i,j,k = 0, 0, 0

                while i < len(l) and j < len(r):
                    if l[i] <= r[j]:
                        nums[k] = l[i]
                        i+=1
                    else: 
                        nums[k] = r[j]
                        j+=1
                    k+=1

                while i < len(l):
                    nums[k] = l[i]
                    i+=1
                    k+=1

                while j < len(r):
                    nums[k] = r[j]
                    j+=1
                    k+=1
        
        mergeSort(nums)
        return nums