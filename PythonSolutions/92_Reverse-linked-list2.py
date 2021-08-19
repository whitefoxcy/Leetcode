# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:09:54 2021

@author: yan_chen
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Iteratively
        # Time: O(N)
        # Space: O(1)

        if left == right:
            return head

        p = dummy = ListNode(0)
        dummy.next = head

        for _ in range(left-1):
            p = p.next

        cur = p.next
        pre = None

        for _ in range(right-left+1):
            cur.next, pre, cur = pre, cur, cur.next

        # [dummy,...p] [pre,...p.next] [cur,...]

        p.next.next = cur
        p.next = pre

        return dummy.next
