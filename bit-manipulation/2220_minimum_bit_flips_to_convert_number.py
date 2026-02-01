class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0
        for i in range(0, 32):
            if ans & (1 << i) != 0:
                count += 1
        print(count)
        return count


s = Solution()
s.minBitFlips(10, 7)
