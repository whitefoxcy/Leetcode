# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:08:29 2021

@author: yan_chen
"""


class Solution:
    def threeSumSmaller(self, nums, target):

        if not nums or len(nums) < 3:
            return 0

        nums.sort()

        ans = 0

        for k in range(2, len(nums)):
            i, j = 0, k-1

            while i < j:
                if nums[i] + nums[j] < target-nums[k]:
                    ans += j - i
                    i += 1
                else:
                    j -= 1
        return ans
