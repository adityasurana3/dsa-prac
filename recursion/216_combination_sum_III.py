from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def helper(self, index, k, n, subset, total, nums):
        if len(subset) == k:
            if total == n:
                self.result.append(subset.copy())
            return
        if index >= len(nums) or total > n:
            return

        subset.append(nums[index])
        total += nums[index]
        self.helper(index + 1, k, n, subset, total, nums)
        e = subset.pop()
        total -= e
        self.helper(index + 1, k, n, subset, total, nums)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        self.helper(0, k, n, [], 0, nums)
        return self.result


s = Solution()
res = s.combinationSum3(3, 9)
print(res)
