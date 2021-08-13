# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:48:26 2021

@author: yan_chen
"""


class Solution:
    def trap(self, height) -> int:

        # Time: O(N)
        # Space: O(1)

        n, res = len(height), 0
        l, r = 0, n-1
        left_max, right_max = height[0], height[n-1]

        while l < r:
            if left_max < right_max:
                res += left_max-height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                res += right_max-height[r]
                r -= 1
                right_max = max(right_max, height[r])

        return res
