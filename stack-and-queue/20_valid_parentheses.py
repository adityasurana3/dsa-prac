class Solution:
    def __init__(self):
        self.items = []
        self.parentheses_dict = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        for i in s:
            par = self.parentheses_dict.get(i)
            if not par:
                self.items.append(i)
            else:
                if len(self.items) == 0:
                    return False
                if self.items[-1] == par:
                    self.items.pop()
                else:
                    return False
        return len(self.items) == 0


s = Solution()
print(s.isValid("[]"))
