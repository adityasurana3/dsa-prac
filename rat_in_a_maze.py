class Solution:

    def __init__(self):
        self.paths = []

    def helper(self, curri, currj, visited, maze, n, path):
        if curri == n - 1 and currj == n - 1:
            self.paths.append(path)
            return

        directions = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]

        for di, dj, move in directions:
            nexti, nextj = curri + di, currj + dj
            if (
                0 <= nexti < n
                and 0 <= nextj < n
                and not visited[nexti][nextj]
                and maze[nexti][nextj] == 1
            ):
                visited[nexti][nextj] = True
                self.helper(nexti, nextj, visited, maze, n, path + move)
                visited[nexti][nextj] = False

    def ratInMaze(self, maze):
        n = len(maze)
        if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return self.paths

        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True

        self.helper(0, 0, visited, maze, n, "")

        return sorted(self.paths)


s = Solution()
maze = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
]
result = s.ratInMaze(maze)
print(result)
