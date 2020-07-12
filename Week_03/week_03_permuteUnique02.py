from typing import List

"""
全排列II
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, sta, res):
            if depth == size:
                res.append(path[:])
                return res
            for i in range(size):
                if not sta[i]:
                    path.append(nums[i])
                    mark = 0
                    for p in res:
                        if path == p[0:len(path)]:
                            mark = 1
                            break
                    if mark == 1:
                        path.pop()
                        continue
                    sta[i] = True
                    dfs(nums, size, depth+1, path, sta, res)
                    sta[i] = False
                    path.pop()
            return res
        size = len(nums)
        sta = [False] * size
        res = []
        if size == 0:
            return []
        dfs(nums, size, 0, [], sta, res)
        return res


if __name__ == '__main__':
    nums = [3,3,0,3]
    solution = Solution()
    res = solution.permuteUnique(nums)
    print(res)