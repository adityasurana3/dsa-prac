from typing import List


class Solution:
    def __init__(self):
        self.mobile_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.result = []

    def helper(self, digits, index, stsfsf):
        if len(digits) == index:
            self.result.append(stsfsf)
        else:
            keyPressed = digits[index]
            possibilities = self.mobile_map.get(keyPressed)
            for i in possibilities:
                self.helper(digits, index + 1, stsfsf + i)

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result

        self.helper(digits, 0, "")
        return self.result


test_cases = ["23", "", "2"]
for test in test_cases:
    s = Solution()
    result = s.letterCombinations(test)
    print(f"Result for '{test}' is: {result}")
