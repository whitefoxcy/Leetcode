# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:13:52 2021

@author: yan_chen
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        i, j, k = 0, 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1

        return nums1[:k]
