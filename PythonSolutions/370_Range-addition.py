# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:57:30 2021

@author: yan_chen
"""


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        res = [0]*(length+1)

        for start, end, v in updates:
            res[start] += v
            if (end + 1) <= length:
                res[end+1] -= v

        add = 0
        for i in range(length):
            add += res[i]
            res[i] = add

        res.pop()
        return res
