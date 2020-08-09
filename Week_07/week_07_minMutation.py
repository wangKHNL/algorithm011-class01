from typing import List
import operator

"""
最小基因变化
"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        str_map = {'A': 'CGT',
                   'C': 'AGT',
                   'G': 'ACT',
                   'T': 'ACG'}
        queue = [(start, 0)]
        while queue:
            current = queue.pop()
            if current[0] == end:
                return current[1]
            for i, s in enumerate(current[0]):
                for element in str_map[s]:
                    new_str = current[0][0:i] + element + current[0][i+1:len(current[0])]
                    if new_str in bank_set:
                        queue.append((new_str, current[1]+1))
                        bank_set.remove(new_str)
        return -1
    # def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    #     bank = set(bank)
    #     if end not in bank:
    #         return -1
    #
    #     change_map = {
    #         "A": "CGT",
    #         "C": "AGT",
    #         "G": "CAT",
    #         "T": "CGA",
    #     }
    #     queue = [(start, 0)]
    #
    #     while queue:
    #         node, step = queue.pop(0)
    #
    #         if node == end:
    #             return step
    #
    #         for i, s in enumerate(node):
    #             for c in change_map[s]:
    #                 new = node[:i] + c + node[i + 1:]
    #                 if new in bank:
    #                     queue.append((new, step + 1))
    #                     bank.remove(new)
    #     return -1


if __name__ == '__main__':
    start = "AAAACCCC"
    end = "CCCCCCCC"
    bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
    solution = Solution()
    print(solution.minMutation(start, end, bank))
