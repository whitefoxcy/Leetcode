# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:51:30 2021

@author: yan_chen
"""

import collections


class Solution:
    def frequencySort(self, s: str) -> str:

        # Bucket Sort
        s_count = collections.Counter(s)

        n = max(s_count.values())

        bucket = [[] for _ in range(n+1)]

        for char, freq in s_count.items():
            bucket[freq].append(char)

        ans = []

        for i in range(len(bucket)-1, 0, -1):
            for c in bucket[i]:
                ans.append(c*i)

        return ''.join(ans)
