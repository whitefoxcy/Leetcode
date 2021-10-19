# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:17:17 2021

@author: yan_chen
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []
        stack = []
        mapping = {}

        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n

            stack.append(n)

        while stack:
            mapping[stack.pop()] = -1

        for num in nums1:
            res.append(mapping[num])

        return res
