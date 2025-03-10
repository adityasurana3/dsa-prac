from typing import List


class Solution:
    '''
    Example 1:

    Input: words = ["leet","code"], x = "e"
    Output: [0,1]
    Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

    Example 2:

    Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
    Output: [0,2]
    Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

    Example 3:

    Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
    Output: []
    Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

    '''

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [idx for idx, word in enumerate(words) if x in word]


s = Solution()
print(s.findWordsContaining(["leet", "code"], 'e'))
