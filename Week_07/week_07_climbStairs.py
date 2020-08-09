from typing import List
import operator

"""
爬楼梯
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.climbStairs(n))
