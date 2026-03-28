from typing import List


class Solution:
    def __init__(self) -> None:
        self.result: List = []

    def helper(self, index: int, num: List[str]):
        if index >= len(num):
            self.result.append("".join(num))
            return
        num[index] = "0"
        self.helper(index + 1, num)
        num[index] = "1"
        self.helper(index + 1, num)
        num[index] = "0"

    def generateBinaryStrings(self, n: int) -> List[List[int]]:
        num = ["0"] * n
        self.helper(0, num)
        return self.result


test_data = 3
s = Solution()
results = s.generateBinaryStrings(test_data)
print(results)
