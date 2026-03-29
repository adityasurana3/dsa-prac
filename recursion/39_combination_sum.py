from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []

    def helper(
        self, index: int, total: int, subset: List, target: int, candidates: List[int]
    ) -> None:
        if index >= len(candidates):
            return
        if total == target:
            self.result.append(subset.copy())
            return
        elif total > target:
            return
        subset.append(candidates[index])
        total += candidates[index]
        self.helper(index, total, subset, target, candidates)
        subset.pop()
        total -= candidates[index]
        self.helper(index + 1, total, subset, target, candidates)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.helper(0, 0, [], target, candidates)
        return self.result


s = Solution()
res = s.combinationSum(candidates=[2, 3, 5], target=8)
print(res)
