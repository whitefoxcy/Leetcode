# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:57:40 2021

@author: yan_chen
"""


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        # Time: O(N)
        # Space: O(1)

        n = len(arr)

        if n <= 1:
            return n

        res, anchor = 1, 0

        for i in range(1, n):
            if arr[i] == arr[i-1]:
                anchor = i

            elif i == n-1 or (arr[i-1]-arr[i])*(arr[i]-arr[i+1]) >= 0:
                res = max(res, i-anchor+1)
                anchor = i

        return res
