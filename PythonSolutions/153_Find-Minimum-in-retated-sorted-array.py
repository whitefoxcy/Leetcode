# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:56:21 2021

@author: yan_chen
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time: O(logN)
        # Space: O(1)

        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] < nums[0]:
                r = mid - 1
            else:
                l = mid + 1
