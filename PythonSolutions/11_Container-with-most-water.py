# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:00:55 2021

@author: yan_chen
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Two-pointers
        # Time: O(N)
        # Space: O(1)

        l, r, maxarea = 0, len(height)-1, 0

        while l < r:
            maxarea = max(maxarea, (r-l)*min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea
