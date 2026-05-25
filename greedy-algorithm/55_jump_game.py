from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        max_index = 0

        for i in range(length):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True


s = Solution()
print(s.canJump(nums=[2, 3, 1, 1, 4]))
