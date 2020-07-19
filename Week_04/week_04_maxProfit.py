from typing import List

"""
买卖股票的最佳时机 II
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        income = 0
        i = 0
        while i < len(prices):
            j = i+1
            if j == len(prices):
                break
            if prices[j] <= prices[i]:
                i = j
                continue
            while j < len(prices)-1:
                if prices[j] < prices[j+1]:
                    j += 1
                else:
                    break
            income += prices[j] - prices[i]
            i = j+1
        return income


if __name__ == '__main__':
    nums = [7,6,4,3,1]
    solution = Solution()
    print(solution.maxProfit(nums))
