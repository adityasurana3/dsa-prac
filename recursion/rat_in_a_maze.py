from typing import List


class Solution:
    def __init__(self):
        self.result: List[str] = []

    def helper(
        self,
        row: int,
        col: int,
        n: int,
        substr: str,
        nums: List[List[int]],
        visited: List[List[int]],
    ):
        if row == n - 1 and col == n - 1:
            self.result.append(substr)
            return

        # Down
        if row + 1 < n and not visited[row + 1][col] and nums[row + 1][col] == 1:
            visited[row][col] = 1
            self.helper(row + 1, col, n, substr + "D", nums, visited)
            visited[row][col] = 0

        # Left
        if col - 1 >= 0 and not visited[row][col - 1] and nums[row][col - 1] == 1:
            visited[row][col] = 1
            self.helper(row, col - 1, n, substr + "L", nums, visited)
            visited[row][col] = 0

        # Right
        if col + 1 < n and not visited[row][col + 1] and nums[row][col + 1] == 1:
            visited[row][col] = 1
            self.helper(row, col + 1, n, substr + "R", nums, visited)
            visited[row][col] = 0

        # Up
        if row - 1 >= 0 and not visited[row - 1][col] and nums[row - 1][col] == 1:
            visited[row][col] = 1
            self.helper(row - 1, col, n, substr + "U", nums, visited)
            visited[row][col] = 0

    def ratInMaze(self, maze: List[List[int]]):
        n = len(maze)
        if maze[0][0] == 0:
            return []
        visited = [[0] * len(maze[i]) for i in range(len(maze))]
        self.helper(0, 0, n, "", maze, visited)
        return self.result


nums = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

s = Solution()
res = s.ratInMaze(nums)
print(res)
