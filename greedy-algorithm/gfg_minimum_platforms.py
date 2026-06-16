from typing import List


class Solution:
    def minPlatform(self, arr: List[int], dep: List[int]):
        arr.sort()
        dep.sort()
        i = j = 0
        platform = 0
        max_platform = 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                platform += 1
                i += 1

            else:
                platform -= 1
                j += 1
            max_platform = max(max_platform, platform)
        return max_platform


s = Solution()
result = s.minPlatform(
    arr=[900, 940, 950, 1100, 1500, 1800], dep=[910, 1200, 1120, 1130, 1900, 2000]
)
print(result)
