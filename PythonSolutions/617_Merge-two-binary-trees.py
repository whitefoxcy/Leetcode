# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:39:21 2021

@author: yan_chen
"""

import collections


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 is None:
            return root2

        stack = collections.deque([(root1, root2)])

        while stack:
            n1, n2 = stack.pop()

            if not n2:
                continue
            n1.val += n2.val

            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))

            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))

        return root1
