from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


s = Solution()
s.singleNumber([4,1,2,1,2])
