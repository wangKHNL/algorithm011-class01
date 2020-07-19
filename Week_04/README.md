学习笔记
题目：岛屿数量
一、题目
给你一个由 '1'（陆地）和'0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。
二、题目理解与思路
岛屿由横向和纵向相连接的'1'组成，在判断岛屿时，从值为'1'的位置出发，需要判断每一个位置周围（上、下、左、右）是否也是'1'，如果是则需要一直连续判断下去，这个问题存在子问题，即对于值为'1'的点，都需要判断其周围数据情况，因此，该解答题目的核心就是利用递归，找出满足条件的岛屿。
三、实现代码（python）
from typing import List

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
四、编码中遇到的问题
1、二维列表行数、列数
列表不同于数组，没有shape属性，因此需要分别用len(grid)、len(grid[0])得到第一维和第二维的列表长度。
2、搜索条件
只有是值为'1'的位置才需要继续判断其周围数据情况，search函数的调用应在条件判断范围内执行。