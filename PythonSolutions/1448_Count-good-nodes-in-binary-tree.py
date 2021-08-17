# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:40:47 2021

@author: yan_chen
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Iteratively, DFS
        # Time: O(N)
        # Space: O(H)

        res = 0
        stack = [(root, float(-inf))]

        while stack:
            curr, max_v = stack.pop()

            if curr.val >= max_v:
                res += 1

            if curr.left:
                stack.append((curr.left, max(max_v, curr.val)))

            if curr.right:
                stack.append((curr.right, max(max_v, curr.val)))

        return res
