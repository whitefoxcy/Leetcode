# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:06:48 2021

@author: yan_chen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def helper(lower, upper):

            if self.idx == n:
                return None

            val = preorder[self.idx]

            if val <= lower or val >= upper:
                return None

            self.idx += 1

            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        n = len(preorder)
        self.idx = 0

        return helper(float('-inf'), float('inf'))
