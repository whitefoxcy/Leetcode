# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:03:08 2021

@author: yan_chen
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(first, curr):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()

        res = []
        backtrack(1, [])
        return res
