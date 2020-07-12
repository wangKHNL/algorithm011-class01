from typing import List

"""
括号生成
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n, n_left, n_right, str):
            if n_left == n and n_right == n:
                res.append(str)
                return res
            if n_left < n:
                dfs(n, n_left + 1, n_right, str+'(')
            if n_right < n_left:
                dfs(n, n_left, n_right + 1, str+')')
        res = []
        dfs(n, 0, 0, '')
        return res


if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.generateParenthesis(n))


# 错误代码
#         def dfs(n, n_left, n_right, str):
#             if n_left == n and n_right == n:
#                 res.append(str)
#                 return res
#             if n_left < n:
#                 n_left += 1 # 错误
#                 str += '(' # 错误
#                 dfs(n, n_left, n_right, str)
#             if n_right < n_left:
#                 n_right += 1 # 错误
#                 str += ')' # 错误
#                 dfs(n, n_left, n_right, str)
# 在满足添加括号（左或者右）条件后，将n_left和str做了修改，导致回溯后，并不是当前的原始状态。
