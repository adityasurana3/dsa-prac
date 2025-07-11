from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def swap(self, nums: List[int], a: int, b: int) -> None:
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def helper(self, nums: List[int], index: int) -> None:
        if index == len(nums) - 1:
            permutation = []
            for i in nums:
                permutation.append(i)
            self.result.append(permutation[:])
        else:
            for i in range(index, len(nums)):
                self.swap(nums, i, index)
                self.helper(nums, index + 1)
                self.swap(nums, i, index)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, 0)
        return self.result


# Test cases
test_cases = [[1,2,3], [0,1],   [1]]
for test in test_cases:
    s = Solution()
    result = s.permute(test)
    print(result)
