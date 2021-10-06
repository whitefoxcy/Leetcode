# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:03:17 2021

@author: yan_chen
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []

        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1

        return res
