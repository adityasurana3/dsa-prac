from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def helper(self, candidates, target, index, combination):
        if target == 0:
            self.ans.append(combination[:])
            return
        if index == len(candidates) or target < 0:
            return

        # Do not pick the current elemint
        self.helper(candidates, target, index+1, combination)
        # Pick the same element
        combination.append(candidates[index])
        self.helper(candidates, target-candidates[index], index, combination)
        combination.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.helper(candidates, target, 0, [])
        return self.ans
    
candidates = [2,3,6,7]
target = 7

s = Solution()
print(s.combinationSum(candidates, target))