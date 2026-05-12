class Solution:
    def brute_force(self, s: str) -> int:
        n = len(s)
        maxi = 0
        for i in range(0, n):
            my_set = set()
            for j in range(i, n):
                if s[j] in my_set:
                    break
                maxi = max(maxi, j - i + 1)
                my_set.add(s[j])
        return maxi

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxi = left = right = 0
        seen = dict()
        while right < n:
            if s[right] in seen:
                left = max(seen[s[right]], left)
            maxi = max(maxi, right - left + 1)
            seen[s[right]] = right
            right += 1
        return maxi


s = Solution()
print(s.lengthOfLongestSubstring("au"))
print(s.brute_force("au"))
