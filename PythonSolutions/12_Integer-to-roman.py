# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:40:03 2021

@author: yan_chen
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        letters = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                   'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''

        for letter, n in zip(letters, nums):
            res += letter*(num//n)
            num %= n
            if num == 0:
                return res
