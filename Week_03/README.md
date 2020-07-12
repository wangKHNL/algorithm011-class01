学习笔记
全排列算法学习和解题思路整理
一、题目
给定一个没有重复数字的序列，返回其所有可能的全排列。
示例：
输入: [1,2,3]
输出:[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
二、题目理解与思路
1、本题目要求输入无重复数字的序列，可以使用列表存储数值，作为程序输入数据；从结果能够看出，每一个位置穷举所有元素，但不能与其他位置元素相同，在生成结果的过程中，相当于逐层生成节点，最终构造出一颗树，以三个元素为例，在生成树的过程中，只保留满足条件的节点。
2、在搜索过程中，重复性体现在节点的生成过程，针对某一个节点状态，当不是叶子节点时，则遍历数字序列中的每一个元素，如果元素不存在于当前节点的列表中，则将添加新元素，然后递归进入下一层。
3、当到达叶子节点后向上回溯时，应恢复到上一层的节点的状态（即各个参数的数值）
三、实现代码（python）
from typing import List

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

四、编码中遇到的问题
1、path变量问题
代码中path参数初始值为[]，该参数在程序执行过程中，始终对应内存中的同一个位置，在程序运行过程中并没有在递归函数中复制参数，因此，结果res中的添加的所有列表元素并不是固定值，而是随着path变化而不停变化，程序结束后，由于path变成空列表[]，导致res中列表元素都为[]。
2、List 初始化方法（初始化固定值的一维数组）
方法一：list1 = [ 初始值 for i in range(数组长度)]
方法二：list2 = [初始值] * 数组长度
3、path.pop()
该方法默认删除List中最后一个元素，如果加入参数，如：path.pop(i),i为索引位置，则删除对应位置的元素。
五、时间复杂度分析
实现算法时间复杂度为：N*logN，N为输入列表元素个数，其中，for循环内需要进行N次操作，而每一次操作的递归深度为logN，因此最终为N*logN的时间复杂度。
六、参考链接
https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/