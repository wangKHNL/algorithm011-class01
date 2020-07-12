from typing import List

"""
全排列
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, sta, res):
            """
            :param nums: 输入数字序列
            :param size: 输入序列元素个数
            :param depth: 搜索的深度
            :param path: 过程中的数字序列
            :param sta: 序列中元素搜索记录，Fslse代表未访问，True代表已经访问过
            :param res: 返回结果
            :return:
            """
            if depth == size:
                res.append(path[:])
                return res
            for i in range(size):
                if not sta[i]:
                    path.append(nums[i])
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
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)