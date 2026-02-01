from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ############## Brute force ####################
        """
        ans = 0
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for key, value in seen.items():
            if value == 2:
                ans ^= key
        return ans
        """
        ans = 0
        seen = set()

        for x in nums:
            if x in seen:
                ans ^= x
            else:
                seen.add(x)

        return ans


s = Solution()
s.singleNumber([1, 2, 1, 3])
