# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:39:36 2021

@author: yan_chen
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count, i = 0, 0
        seen = {}

        for j, c in enumerate(s):

            if c in seen:
                i = max(i, seen[c])

            count = max(count, j-i+1)

            seen[c] = j + 1

        return count
