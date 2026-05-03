from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass

    def brute_force(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans[i] = nums2[j]
                    break
        return ans


s = Solution()
nums1=[4, 1, 2], nums2=[1, 3, 4, 2]
print(s.nextGreaterElement(nums1=nums1, nums2=nums2))
