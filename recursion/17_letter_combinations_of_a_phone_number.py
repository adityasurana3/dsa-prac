from typing import List


class Solution:
    def __init__(self):
        self.charmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.result = []

    def solve(self, index, digits, subset):
        if index >= len(digits):
            self.result.append("".join(subset))
            return
        for i in self.charmap[digits[index]]:
            subset.append(i)
            self.solve(index + 1, digits, subset)
            subset.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        self.solve(0, digits, [])
        return self.result


s = Solution()
res = s.letterCombinations("23")
print(res)
