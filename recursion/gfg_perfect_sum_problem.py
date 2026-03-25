from typing import List


class Solution:
    def __init__(self) -> None:
        self.result: List = []
        self.count: int = 0

    def helper(
        self,
        candidates: List[int],
        index: int,
        total: int,
        currentFormation: List,
        target: int,
    ):
        if target == total:
            return 1
        elif total > target:
            return 0
        if index >= len(candidates):
            return 0
        currentFormation.append(candidates[index])
        sum_ = total + candidates[index]
        pick = self.helper(candidates, index + 1, sum_, currentFormation, target)
        e = currentFormation.pop()
        sum_ -= e
        not_pick = self.helper(candidates, index + 1, sum_, currentFormation, target)
        return pick + not_pick

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helper(
            candidates=candidates, index=0, total=0, currentFormation=[], target=target
        )


test_data = [
    ([5, 2, 3, 10, 6, 8], 10),
    ([2, 5, 1, 4, 3], 10),
    ([5, 7, 8], 3),
    ([35, 2, 8, 22], 0),
]
for t, k in test_data:
    s = Solution()
    results = s.combinationSum(candidates=t, target=k)
    print(results)
