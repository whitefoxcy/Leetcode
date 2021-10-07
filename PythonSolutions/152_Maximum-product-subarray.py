# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:30:16 2021

@author: yan_chen
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        min_so_far, max_so_far = nums[0], nums[0]

        res = max_so_far

        for i in range(1, n):
            curr = nums[i]

            max_so_far, min_so_far = max(curr, curr*max_so_far, curr*min_so_far), \
                min(curr, curr*max_so_far, curr*min_so_far)
            res = max(res, max_so_far)

        return res
