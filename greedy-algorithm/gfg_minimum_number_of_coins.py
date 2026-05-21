class Solution:
    def findMin(self, n: int) -> int:
        currency = (1, 2, 5, 10)
        total_len = len(currency)
        count = 0
        for i in range(total_len - 1, -1, -1):
            while n >= currency[i]:
                n -= currency[i]
                count += 1
        return count


s = Solution()
print(s.findMin(121))
