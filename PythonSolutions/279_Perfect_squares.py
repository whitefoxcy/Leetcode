# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:51:00 2021

@author: yan_chen
"""


class Solution:
    def numSquares(self, n: int) -> int:

        squares = [i*i for i in range(1, int(n**0.5)+1)]

        q = {n}

        level = 0

        while q:
            level += 1
            next_q = set()
            for reminder in q:
                for square in squares:
                    if reminder == square:
                        return level
                    elif reminder < square:
                        break
                    else:
                        next_q.add(reminder-square)
            q = next_q

        return level
