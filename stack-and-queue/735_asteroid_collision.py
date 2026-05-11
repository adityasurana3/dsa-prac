from typing import List


class Solution:
    def __init__(self) -> None:
        self.stack = []

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        for i in range(0, n):
            num = asteroids[i]
            if num > 0:
                self.stack.append(num)
                continue
            while self.stack and self.stack[-1] > 0 and self.stack[-1] < abs(num):
                self.stack.pop()
            if self.stack and self.stack[-1] > 0 and self.stack[-1] == abs(num):
                self.stack.pop()
            elif not self.stack or self.stack[-1] < 0:
                self.stack.append(num)
        return self.stack


s = Solution()
print(s.asteroidCollision(asteroids=[-2, -2, 1, -2]))
