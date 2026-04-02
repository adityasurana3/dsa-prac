from typing import List


class Solution:
    def __init__(self):
        self.result: List[str] | None = []

    def helper(
        self, index: int, subset: List[int] | None, nums: List[int], sum_=0
    ) -> None:
        if index >= len(nums):
            self.result.append(sum_)
            sum_ = 0
            return
        subset.append(nums[index])
        sum_ += nums[index]
        self.helper(index + 1, subset, nums, sum_=sum_)
        e = subset.pop()
        sum_ -= e
        self.helper(index + 1, subset, nums, sum_=sum_)

    def generateParenthesis(self, n: List[int]) -> List[str]:
        self.helper(0, [], n)
        return self.result


nums = [2,3]
s = Solution()
res = s.generateParenthesis(nums)
print(res)
