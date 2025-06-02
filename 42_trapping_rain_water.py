from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        max_right = [0] * n
        max_left = [0] * n

        max_left[0] = height[0]
        max_right[-1] = height[-1]
        sum_ = 0

        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i - 1])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])

        for i in range(n):
            sum_ += min(max_left[i], max_right[i]) - height[i]

        return sum_


s = Solution()
result = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

print(result)
