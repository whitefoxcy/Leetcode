# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 16:27:56 2021

@author: yan_chen
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        stack, node = [], root
        head = Node(None)
        prev = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if not head.right:
                head.right = node

            if prev:
                prev.right, node.left = node, prev
            prev = node
            node = node.right

        prev.right = head.right
        head.right.left = prev

        return head.right
