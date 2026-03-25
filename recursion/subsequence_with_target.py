from typing import List


class Solution:
    def __init__(self) -> None:
        self.result: List = []

    def helper(
        self,
        candidates: List[int],
        index: int,
        total: int,
        currentFormation: List,
        target: int,
    ):
        if total == target:
            self.result.append(currentFormation.copy())
            return
        elif total > target:
            return
        if index >= len(candidates):
            return

        currentFormation.append(candidates[index])
        sum_ = total + candidates[index]
        self.helper(candidates, index + 1, sum_, currentFormation, target)
        e = currentFormation.pop()
        sum_ -= e
        self.helper(candidates, index + 1, sum_, currentFormation, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.helper(
            candidates=candidates, index=0, total=0, currentFormation=[], target=target
        )
        return self.result


test_data = [
    ([17, 18, 6, 11, 2, 4], 6),
    ([1, 2, 3], 3)
    ]
for t, k in test_data:
    s = Solution()
    results = s.combinationSum(candidates=t, target=k)
    print(results)
