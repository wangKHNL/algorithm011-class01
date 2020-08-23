from typing import List
import operator
import numpy as np
import queue

"""
反转字符串 II
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        begin = 0
        mid = k
        end = 2 * k
        while end <= len(s):
            # 反转前 k 个字符
            i = mid -1
            str_temp = ''
            while i >= begin:
                str_temp = str_temp + s[i]
                i -= 1
            s = s[0:begin] + str_temp + s[mid:len(s)]

            begin = end
            mid = begin + k
            end = mid + k
        if mid >= len(s):
            # 全部反转
            i = len(s)-1
            str_temp = ''
            while i >= begin:
                str_temp = str_temp + s[i]
                i -= 1
            s = s[0:begin] + str_temp
        if mid < len(s) and len(s) <= end:
            # 反转前k个字符
            i = mid - 1
            str_temp = ''
            while i >= begin:
                str_temp = str_temp + s[i]
                i -= 1
            s = s[0:begin] + str_temp + s[mid:len(s)]
        return s


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    sol = Solution()
    print(sol.reverseStr(s,k))
