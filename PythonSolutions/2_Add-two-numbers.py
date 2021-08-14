# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 10:49:35 2021

@author: yan_chen
"""


class Solution:
    def addTwoNumbers(self, l1, l2) -> Optional[ListNode]:

        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10

        return dummy.next
