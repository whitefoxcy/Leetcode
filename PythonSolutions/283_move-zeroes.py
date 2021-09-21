# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:07:32 2021

@author: yan_chen
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero != i:
                    nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
