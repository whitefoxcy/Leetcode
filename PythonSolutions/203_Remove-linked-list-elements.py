# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:16:36 2021

@author: yan_chen
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return head

        Dummy = ListNode(None, head)
        Dummy.next = head

        prev, curr = Dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return Dummy.next
