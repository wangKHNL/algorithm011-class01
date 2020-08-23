from typing import List
import operator
import numpy as np
import queue

"""
字符串中的第一个唯一字符
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for index,str_tem in enumerate(s):
            if str_tem in hash_map.keys():
                hash_map[str_tem] = -1
            else:
                hash_map[str_tem] = index
        for key in hash_map:
            if hash_map[key] > -1:
                return hash_map[key]
        return -1


if __name__ == '__main__':
    s = "loveleetcode"
    sol = Solution()
    print(sol.firstUniqChar(s))
