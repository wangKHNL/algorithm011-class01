"""
二叉树的前序遍历
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def lookup(root):
            if not root:
                return
            else:
                res.append(root.val)
            lookup(root.left)
            lookup(root.right)
            return res
        lookup(root)
        return res