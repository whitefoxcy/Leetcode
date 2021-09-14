# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:11:35 2021

@author: yan_chen
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)
