# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:16:46 2021

@author: yan_chen
"""


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:

        # Time: O(N^2)
        # Space: O(N)

        banned = {tuple(mine) for mine in mines}
        res = 0
        grid = [[0]*n for _ in range(n)]

        for r in range(n):

            left = 0
            for c in range(n):
                left = 0 if (r, c) in banned else left+1
                grid[r][c] = left

            right = 0
            for c in range(n-1, -1, -1):
                right = 0 if (r, c) in banned else right+1
                if grid[r][c] > right:
                    grid[r][c] = right

        for c in range(n):

            d = 0
            for r in range(n):
                d = 0 if (r, c) in banned else d+1
                if grid[r][c] > d:
                    grid[r][c] = d

            u = 0
            for r in range(n-1, -1, -1):
                u = 0 if (r, c) in banned else u+1
                if grid[r][c] > u:
                    grid[r][c] = u
                if grid[r][c] > res:
                    res = grid[r][c]

        return res
