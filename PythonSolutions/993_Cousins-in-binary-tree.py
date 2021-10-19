# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:06:56 2021

@author: yan_chen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        res = []

        q = deque([(root, None, 0)])

        while q:

            if len(res) == 2:
                break

            node, parent, level = q.popleft()

            if node.val in [x, y]:
                res.append((parent, level))

            if node.left:
                q.append([node.left, node, level+1])

            if node.right:
                q.append([node.right, node, level+1])

        x_node, y_node = res

        return x_node[0] != y_node[0] and x_node[1] == y_node[1]
