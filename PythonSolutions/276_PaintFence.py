# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:42:49 2021

@author: yan_chen
"""
from functools import cache


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k*k

            return (k-1)*(total_ways(i-1)+total_ways(i-2))

        return total_ways(n)
