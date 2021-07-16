# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:04:44 2021

@author: yan_chen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative

        res, stack = [], []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right

        return res
