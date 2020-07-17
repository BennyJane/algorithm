'''
Function:
    二叉树的镜像
Author:
    Charles
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(root):
            if not root: return
            root.left, root.right = root.right, root.left
            recur(root.left)
            recur(root.right)
        recur(root)
        return root