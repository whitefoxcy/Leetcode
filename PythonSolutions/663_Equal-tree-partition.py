# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:10:54 2021

@author: yan_chen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:

        sub_total = []

        def treeSum(subroot):
            if not subroot:
                return 0
            left_tree = subroot.left
            right_tree = subroot.right
            sub_sum = subroot.val + treeSum(left_tree) + treeSum(right_tree)
            sub_total.append(sub_sum)
            return sub_sum

        treeSum(root)
        total = sub_total.pop()

        if total % 2 != 0:
            return False

        return total/2 in sub_total
