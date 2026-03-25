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
    ) -> bool:
        if target == total:
            return True
        elif total > target:
            return False
        if index == len(candidates):
            return False
        currentFormation.append(candidates[index])
        sum_ = total + candidates[index]
        pick = self.helper(candidates, index + 1, sum_, currentFormation, target)
        if pick == True:
            return True
        e = currentFormation.pop()
        sum_ -= e
        not_pick = self.helper(candidates, index + 1, sum_, currentFormation, target)
        return not_pick

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helper(
            candidates=candidates, index=0, total=0, currentFormation=[], target=target
        )


test_data = [([10, 1, 2, 7, 6, 1, 5], 8), ([2, 3, 5, 7, 9], 100)]
for t, k in test_data:
    s = Solution()
    results = s.combinationSum(candidates=t, target=k)
    print(results)
