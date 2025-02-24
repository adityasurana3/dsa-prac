from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m-1
        q = n-1
        r = len(nums1) -1
        while(r >= 0):
            if (q < 0): break
            if (p >= 0 and nums1[p] > nums2[q]):
                nums1[r] = nums1[p]
                r -= 1
                p -= 1
            else:
                nums1[r] = nums2[q]
                r -= 1
                q -= 1
        print(nums1)

s = Solution()
s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
