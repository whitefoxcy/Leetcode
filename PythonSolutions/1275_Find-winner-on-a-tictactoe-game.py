# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:23:29 2021

@author: yan_chen
"""


class Solution:
    def tictactoe(self, moves) -> str:

        n = 3

        rows = [0]*n
        cols = [0]*n
        d1, d2 = 0, 0

        for i, move in enumerate(moves):
            r, c = move

            sign = 1 if i % 2 == 0 else -1

            rows[r] += sign
            cols[c] += sign
            if r == c:
                d1 += sign
            if r + c == n-1:
                d2 += sign

            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(d1) == 3 or abs(d2) == 3:
                return 'A' if sign == 1 else 'B'

        if len(moves) == n**2:
            return 'Draw'
        else:
            return 'Pending'
