# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:18:05 2021

@author: yan_chen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def pathSum(node):

            if not node:
                return 0

            left_sum = max(0, pathSum(node.left))
            right_sum = max(0, pathSum(node.right))
            self.res = max(self.res, node.val+left_sum+right_sum)

            return node.val+max(left_sum, right_sum)

        self.res = float('-inf')
        pathSum(root)
        return self.res
