class Solution:
    '''
    Example 1:

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

    Example 2:

    Input: s = "cbbd"
    Output: "bb"

    '''

    ############################ SOLUTION 1 -> Time complexity(O(n^3)) ############################
    '''
    def isPalindrome(self, a):
        i = 0
        j = len(a) - 1
        while(i<j):
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        longestSubStrPalindrome = '0'
        len_ = len(s)
        for i in range(len_):
            sub_str = ''
            for j in range(i, len_):
                sub_str += s[j]
                if(self.isPalindrome(sub_str) and len(sub_str) > len(longestSubStrPalindrome)):
                    longestSubStrPalindrome = sub_str
        return longestSubStrPalindrome
    '''

    ############################ SOLUTION 2 -> Time complexity(O(n^2)) ############################
    def longestPalindrome(self, s: str) -> str:
        # Generate the longest odd length palindrome string
        str_len = len(s)
        ans = ''
        max_len = 0
        for mid in range(str_len):
            i = mid - 1
            j = mid + 1
            currLen = 1
            while i >= 0 and j < str_len and s[i] == s[j]:
                i -= 1
                j += 1
                currLen += 2
            if (currLen > max_len):
                ans = s[i+1:j]
                max_len = currLen

        # Generate longest even length palindrome string
        for mid in range(str_len):
            i = mid
            j = mid + 1
            currLen = 0
            while i >= 0 and j < str_len and s[i] == s[j]:
                i -= 1
                j += 1
                currLen += 2
            if (currLen > max_len):
                ans = s[i+1:j]
                max_len = currLen

        return ans


s = Solution()

print(s.longestPalindrome('babad'))
