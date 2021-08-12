# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:07:46 2021

@author: yan_chen
"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = collections.Counter(s)

        for i, v in enumerate(s):
            if count[v] == 1:
                return i

        return -1
