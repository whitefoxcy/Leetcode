# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:47:11 2021

@author: yan_chen
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Time: O(M*N)
        # Space: O(1)

        res = []
        m, n = len(matrix), len(matrix[0])
        row_begin, col_begin = 0, 0
        row_end, col_end = m-1, n-1

        while row_begin <= row_end and col_begin <= col_end:
            # from left to right
            for j in range(col_begin, col_end+1):
                res.append(matrix[row_begin][j])
            row_begin += 1

            # from up to botton
            for i in range(row_begin, row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1

            # from right to left
            if row_end >= row_begin:
                for j in range(col_end, col_begin-1, -1):
                    res.append(matrix[row_end][j])
                row_end -= 1

            # from botton to up
            if col_begin <= col_end:
                for i in range(row_end, row_begin-1, -1):
                    res.append(matrix[i][col_begin])
                col_begin += 1

        return res
