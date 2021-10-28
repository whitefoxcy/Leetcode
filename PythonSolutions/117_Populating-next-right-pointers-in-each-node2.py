# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:52:52 2021

@author: yan_chen
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        leftmost = root

        while leftmost:
            prev, curr = None, leftmost

            leftmost = None

            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
        return root

    def processChild(self, childNode, prev, leftmost):

        if childNode:
            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            prev = childNode

        return prev, leftmost
