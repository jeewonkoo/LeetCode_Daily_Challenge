class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_1, ptr_2 = m-1, n-1
        idx = len(nums1)-1
        while ptr_2 >= 0:
            # print(ptr_1, ptr_2, idx, nums1)
            if ptr_1 >= 0 and nums1[ptr_1] >= nums2[ptr_2]:
                nums1[idx] = nums1[ptr_1]
                ptr_1 -= 1
                
            else: 
                nums1[idx] = nums2[ptr_2]
                ptr_2 -= 1
                
            idx -=1 