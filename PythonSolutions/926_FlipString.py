# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:23:16 2021

@author: yan_chen
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        res = cnt0 = s.count('0')

        for c in s:
            if c == '1':
                cnt0 += 1
            else:
                cnt0 -= 1
            res = min(res, cnt0)

        return res
