from typing import List
import operator
import numpy as np

"""
有效的字母异位词
"""


class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        """
        可实现，但是时间复杂度较高，超出时间
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        t_b = [True]*len(t)
        b = False
        for i in s:
            for j_pos, j in enumerate(t):
                if t_b[j_pos]:
                    if i == j:
                        b = True
                        t_b[j_pos] = False
                        break
            if not b:
                return b
        if np.sum(np.array(t_b) == 1) == 0:
            return True
        else:
            return False

    def isAnagram_2(self, s: str, t: str) -> bool:
        """
        根据26个字母的位置，记录个数，在s中字母记录加1 ，在t中的字母减1 ；
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        l_str = [0]*26
        for i in s:
            l_str[ord(i)-97] += 1
        for j in t:
            l_str[ord(j)-97] -= 1

        if np.sum(np.array(l_str) == 0) == 26:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "rat"
    t = "tar"
    solution = Solution()
    print(solution.isAnagram_2(s, t))
