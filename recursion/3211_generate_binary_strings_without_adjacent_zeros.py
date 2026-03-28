from typing import List


class Solution:
    def __init__(self):
        self.result: List[str] = []

    def helper(self, index: int, flag: bool, num):
        if index >= len(num):
            self.result.append("".join(num))
            return
        num[index] = "1"
        self.helper(index + 1, True, num)
        if flag == True:
            num[index] = "0"
            self.helper(index + 1, False, num)
            num[index] = "1"

    def validStrings(self, n: int) -> List[str]:
        num = ["1"] * n
        self.helper(0, True, num)
        return self.result


test_data = 3
s = Solution()
results = s.validStrings(test_data)
print(results)
