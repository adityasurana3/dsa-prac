from typing import List


class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns the indices of the two numbers in the list that add up to the target.
        
        Args:
            nums (List[int]): List of integers.
            target (int): The target sum.
        
        Returns:
            List[int]: Indices of the two numbers adding up to target.
        """
        result_dict = {}
        for idx, i in enumerate(nums):
            result = target - i
            if result in result_dict:
                return result_dict[result], idx
            result_dict[i] = idx
        return []


s = Solution()
result = s.twoSum([2,7,11,15], 9)
print(result)
