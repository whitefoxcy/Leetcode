# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:15:50 2021

@author: yan_chen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        if n == 0:
            return []
        else:
            return self.helper(1, n)

    def helper(self, start, end):
        all_trees = []
        if start > end:
            return [None]
        for rootval in range(start, end+1):
            left_trees = self.helper(start, rootval-1)
            right_trees = self.helper(rootval+1, end)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(rootval)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)
        return all_trees
