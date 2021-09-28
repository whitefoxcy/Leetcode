# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:34:20 2021

@author: yan_chen
"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        j = 1

        for i in range(0, len(nums), 2):
            if nums[i] % 2:
                while nums[j] % 2:
                    j += 2

                nums[i], nums[j] = nums[j], nums[i]

        return nums
