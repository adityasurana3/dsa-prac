from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        count = left = right = 0
        g.sort()
        s.sort()
        while left < n and right < m:
            if g[left] <= s[right]:
                count += 1
                left += 1
            right += 1
        return count


s = Solution()
lst = [([1, 2, 3], [1, 1]), ([1, 2, 3], [3]), ([1, 2], [1, 2, 3])]
for a, b in lst:
    print(s.findContentChildren(g=a, s=b))
