from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left_sum = right_sum = maxi = 0
        if n == k:
            return sum(cardPoints)
        for i in range(0, k):
            left_sum += cardPoints[i]
        maxi = left_sum
        right_index = n - 1
        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_index]
            maxi = max(maxi, left_sum + right_sum)
            right_index -= 1
        return maxi


s = Solution()
print(s.maxScore([1, 2, 3, 4, 5, 6, 1], k=3))
