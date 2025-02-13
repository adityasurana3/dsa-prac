from typing import List


class Solution:
    def __init__(self):
        self.finalAns = []
    
    def helper(self, nums: List[int], index: int, currentFormation: List):
        # Base condition
        if(len(nums) ==  index):
            self.finalAns.append(currentFormation[:])
            return
        
        # If we pick the element
        currentFormation.append(nums[index])
        self.helper(nums, index+1, currentFormation)
        currentFormation.pop()

        # Do not pick the element
        self.helper(nums, index+1, currentFormation)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, 0, [])
        return self.finalAns

nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))