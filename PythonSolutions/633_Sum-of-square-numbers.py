# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:44:31 2021

@author: yan_chen
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        min_v = 0
        max_v = math.floor(math.sqrt(c))

        for i in range(min_v, max_v+1):
            j = math.sqrt(c-i**2)
            if j == int(j):
                return True

        return False
