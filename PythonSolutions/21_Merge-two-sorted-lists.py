# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:01:37 2021

@author: yan_chen
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Iterative
        # Time: O(m+n)
        # Space: O(1)

        curr = ListNode(-1)
        Dummy = curr

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return Dummy.next
