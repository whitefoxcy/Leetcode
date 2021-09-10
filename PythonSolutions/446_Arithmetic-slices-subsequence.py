# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 12:14:33 2021

@author: yan_chen
"""
import collections


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(n)]

        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]

                dp[i][diff] += cnt + 1
                ans += cnt

        return ans
