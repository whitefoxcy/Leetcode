# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:47:25 2021

@author: yan_chen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        self.maxPath(root)
        return self.res

    def maxPath(self, node):

        if not node:
            return 0

        l = self.maxPath(node.left)
        r = self.maxPath(node.right)

        self.res = max(self.res, l+r)

        return max(l, r) + 1
