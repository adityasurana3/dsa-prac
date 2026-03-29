from typing import List


class Solution:
    def __init__(self):
        self.result: List[str] | None = []

    def helper(self, index: int, total: int, list_num: List[str]) -> None:
        if index >= len(list_num):
            if total == 0:
                self.result.append("".join(list_num))
            return
        if total > len(list_num) // 2:
            return
        elif total < 0:
            return
        list_num[index] = "("
        self.helper(index + 1, total + 1, list_num)
        list_num[index] = ")"
        self.helper(index + 1, total - 1, list_num)

    def generateParenthesis(self, n: int) -> List[str]:
        num = [""] * n * 2
        self.helper(0, 0, num)
        return self.result


s = Solution()
res = s.generateParenthesis(3)
print(res)
