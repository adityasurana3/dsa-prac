from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        ############################## Brute force approach(O(n^2)) ###########################################
            max_sub_arr = -1
            n = len(nums)
            for i in range(n):
                zeros = 0
                ones = 0
                for j in range(i, n):
                    if nums[j] == 0:
                        zeros += 1
                    else:
                        ones += 1
                if zeros == ones:
                    max_sub_arr = max(max_sub_arr, j - i + 1)
            return max_sub_arr
        """
        sum_ = 0
        maxLength = 0
        result_sum = {0: -1}
        for idx, i in enumerate(nums):
            sum_ += 1 if i == 0 else -1
            if result_sum.get(sum_) is not None:
                maxLength = max(idx - result_sum.get(sum_), maxLength)
            else:
                result_sum[sum_] = idx
        return maxLength


s = Solution()
print(s.findMaxLength([0, 0, 1]))
