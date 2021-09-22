# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:02:36 2021

@author: yan_chen
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # dfs
        # Time: O(m*n)
        # Space O(m*n)

        m, n = len(grid), len(grid[0])
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
        return maxArea

    def dfs(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0

        grid[i][j] = '#'
        area = 1
        area += self.dfs(grid, i-1, j) + self.dfs(grid, i+1, j) + self.dfs(grid, i, j-1) \
            + self.dfs(grid, i, j+1)
        return area
