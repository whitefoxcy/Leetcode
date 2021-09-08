# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:52:21 2021

@author: yan_chen
"""


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        # Time: O(N)
        # Space: O(N)

        n = len(shifts)

        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]

        res = []

        for i, c in enumerate(s):
            index = (ord(c)-ord('a') + shifts[i]) % 26
            res.append(chr(index+ord('a')))

        return ''.join(res)
