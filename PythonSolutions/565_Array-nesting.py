# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:28:13 2021

@author: yan_chen
"""


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        res = 0

        for i in range(len(nums)):
            if nums[i] != -1:
                start, count = i, 0
                while nums[start] != -1:
                    temp = start
                    start = nums[start]
                    nums[temp] = -1
                    count += 1
                res = max(res, count)

        return res
