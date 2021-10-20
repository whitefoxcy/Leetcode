# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:51:01 2021

@author: yan_chen
"""


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        # Time O(m+n)
        # Space O(m+n)

        res = []

        if not firstList or not secondList:
            return res

        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):

            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])

            if lo <= hi:
                res.append([lo, hi])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res
