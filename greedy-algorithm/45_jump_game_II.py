from typing import List


class Recursion:
    def __init__(self) -> None:
        self.min_jumps = float("inf")

    def _find_min_jump(self, index: int, jumps: int, nums: List[int]) -> None:
        last_index = len(nums) - 1

        if index >= last_index:
            self.min_jumps = min(self.min_jumps, jumps)
            return

        if jumps >= self.min_jumps:
            return

        max_jump = nums[index]

        for step in range(1, max_jump + 1):
            self._find_min_jump(
                index=index + step,
                jumps=jumps + 1,
                nums=nums,
            )

    def jump(self, nums: List[int]) -> int:
        self._find_min_jump(index=0, jumps=0, nums=nums)
        return self.min_jumps


class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        jumps = 0
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1
        return jumps


s = Recursion()
print(s.jump(nums=[2, 1]))

s = Solution()
print(s.jump(nums=[2, 1]))
