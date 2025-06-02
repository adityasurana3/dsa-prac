from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left_prod = 1
        ans = [1] * n

        for i in range(len(nums) - 2, -1, -1):
            ans[i] = nums[i + 1] * ans[i + 1]

        for i in range(n):
            right_prod = 1 if i == len(nums) - 1 else ans[i]
            ans[i] = left_prod * right_prod
            left_prod *= nums[i]

        return ans

        """
        ans = []
        left_pref_mul = [1] * len(nums)
        right_pref_mul = [1] * len(nums)
        left_pref_mul[0] = nums[0]

        left_pref_mul[0] = nums[0]

        for i in range(len(nums)):
            left_pref_mul[i] = nums[i] * left_pref_mul[i - 1]

        right_pref_mul[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right_pref_mul[i] = nums[i] * right_pref_mul[i + 1]

        for i in range(len(nums)):
            left_prod = 1 if i == 0 else left_pref_mul[i - 1]
            right_prod = 1 if i == len(nums) - 1 else right_pref_mul[i + 1]
            ans.append(left_prod * right_prod)

        return ans
        """


s = Solution()
result = s.productExceptSelf([-1, 1, 0, -3, 3])
print(result)
