# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:46:01 2021

@author: yan_chen
"""
from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        empty = 2**31-1
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            r, c = queue.popleft()
            for dr, dc in direction:
                new_r, new_c = r+dr, c+dc
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols or rooms[new_r][new_c] != empty:
                    continue
                rooms[new_r][new_c] = rooms[r][c]+1
                queue.append((new_r, new_c))


rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
test = Solution()

test.wallsAndGates(rooms)
