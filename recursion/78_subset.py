from typing import List


class Solution:
    def __init__(self):
        self.finalAns: List = []

    def helper(self, nums: List[int], index: int, currentFormation: List):
        if index == len(nums):
            self.finalAns.append(currentFormation.copy())
            return
        # To pick the element
        currentFormation.append(nums[index])
        self.helper(nums, index + 1, currentFormation)
        # To not pick the element
        currentFormation.pop()
        self.helper(nums, index + 1, currentFormation)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, 0, [])
        return self.finalAns


nums = [5, 8, 9]
solution = Solution()
print(solution.subsets(nums))
