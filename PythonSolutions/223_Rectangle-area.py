# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:08:00 2021

@author: yan_chen
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        overlap = max(min(bx2, ax2)-max(bx1, ax1), 0) * \
            max(min(by2, ay2) - max(by1, ay1), 0)

        return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) - overlap
