from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        result_dict = {0: -1}
        # prefix_sum = [0] * len(nums)
        sum_ = 0
        maxLen = 0
        for idx, i in enumerate(nums):
            sum_ += i
            # if idx == 0:
            #     prefix_sum[idx] = i
            # else:
            #     prefix_sum[idx] = i + prefix_sum[idx - 1]

            valueNeedToSub = sum_ - k

            if result_dict.get(valueNeedToSub) is not None:
                maxLen = max(idx - result_dict.get(valueNeedToSub), maxLen)
            if result_dict.get(sum_) is None:
                result_dict[sum_] = idx
        return maxLen


s = Solution()
result = s.maxSubArrayLen([1, -1, 5, -2, 3], k=3)
print(result)
