# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:37:38 2021

@author: yan_chen
"""

import collections


class Solution:
    def canReorderDoubled(self, arr) -> bool:

        # Time: O(N+k*logk)

        d = collections.Counter(arr)

        for num in sorted(d, key=abs):
            if d[num] > d[num*2]:
                return False
            d[num*2] -= d[num]

        return True
