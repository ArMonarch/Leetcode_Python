from collections import deque
from unittest import TestCase


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        return self.method_02(grid)

    def method_01(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island = 0

        def dfs(i: int, j: int) -> None:
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i - 1 >= 0: dfs(i - 1, j)
                if i + 1 < n: dfs(i + 1, j)
                if j - 1 >= 0: dfs(i, j - 1)
                if j + 1 < m: dfs(i, j + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i, j)

        return island

    def method_02(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    island += 1
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.pop()
                        grid[x][y] = "0"
                        if x - 1 >= 0 and grid[x - 1][y] == "1": queue.append((x - 1, y))
                        if x + 1 < n and grid[x + 1][y] == "1": queue.append((x + 1, y))
                        if y - 1 >= 0 and grid[x][y - 1] == "1": queue.append((x, y - 1))
                        if y + 1 < m and grid[x][y + 1] == "1": queue.append((x, y + 1))

        return island
        

class Tests(TestCase):
    def test_case_01(self) -> None:
        grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        expected = 1

        numIslands = Solution().numIslands
        self.assertEqual(expected, numIslands(grid))

    def test_case_02(self) -> None:
        grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        expected = 3

        numIslands = Solution().numIslands
        self.assertEqual(expected, numIslands(grid))
