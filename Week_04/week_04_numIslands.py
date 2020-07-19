from typing import List

"""
岛屿数量
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search(grid, m, n):
            if grid[m][n] == '1':
                grid[m][n] = '0'
                if m + 1 < len(grid):
                    search(grid, m + 1, n)
                if m - 1 >= 0:
                    search(grid, m - 1, n)
                if n + 1 < len(grid[0]):
                    search(grid, m, n + 1)
                if n - 1 >= 0:
                    search(grid, m, n - 1)
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num += 1
                    search(grid, i, j)
        return num


if __name__ == '__main__':
    inPut = \
        [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
    solution = Solution()
    print(solution.numIslands(inPut))
