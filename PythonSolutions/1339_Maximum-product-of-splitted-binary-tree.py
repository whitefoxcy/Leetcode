# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:32:56 2021

@author: yan_chen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxProduct(self, root) -> int:

        subtotal = []

        def treeSum(subroot):
            if subroot == None:
                return 0
            left_tree = treeSum(subroot.left)
            right_tree = treeSum(subroot.right)
            subsum = subroot.val + left_tree + right_tree
            subtotal.append(subsum)
            return subsum

        total = treeSum(root)
        res = 0

        for s in subtotal:
            res = max(res, s*(total-s))

        return res % (10**9+7)
