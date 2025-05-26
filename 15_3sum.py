from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], idx: int, target: int, ans: List[List[int]]) -> None:
        b = idx
        c = len(nums) - 1
        while b < c:
            if nums[b] + nums[c] == target:
                lst = [-target, nums[b], nums[c]]
                ans.append(lst)
                b += 1
                c -= 1
                while b < c and nums[b] == nums[b - 1]:
                    b += 1
                while b < c and nums[c] == nums[c + 1]:
                    c -= 1
            elif nums[b] + nums[c] > target:
                c -= 1
            else:
                b += 1
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i + 1, -nums[i], ans)
        return ans
    

s = Solution()
result = s.threeSum([-1, 0, 1, 2, -1, -4])
print(result)

# Solution 1: You can use brute force approach using three loops time complexity will be O(N^3)
# Solution 2: You can use twoSum to calculate the a we know that a+b+c= 0 the b+c = -a time complexity will we O(N^2)