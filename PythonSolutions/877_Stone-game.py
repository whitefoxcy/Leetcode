# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:15:45 2021

@author: yan_chen
"""


class Solution:
    def stoneGame(self, piles) -> bool:

        n = len(piles)
        dp = piles[:]

        for d in range(1, n):
            for i in range(n-d):
                dp[i] = max(piles[i]-dp[i+1], piles[i+d]-dp[i])

        return dp[0] > 0
