# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:46:24 2021

@author: yan_chen
"""

import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])

        fresh = 0
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        t = 0

        while q and fresh > 0:
            t += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in d:
                    new_x, new_y = x+dx, y+dy

                    if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols and grid[new_x][new_y] == 1:

                        grid[new_x][new_y] = 2
                        fresh -= 1
                        q.append((new_x, new_y))

        return t if fresh == 0 else -1
