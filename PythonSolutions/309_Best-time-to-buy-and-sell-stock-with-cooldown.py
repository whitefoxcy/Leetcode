# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:20:19 2021

@author: yan_chen
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        held, sold, rest = float('-inf'), 0, 0

        for price in prices:
            held, sold, rest = max(held, rest-price), held + \
                price, max(rest, sold)

        return max(rest, sold)
