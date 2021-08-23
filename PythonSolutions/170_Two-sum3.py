# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:15:22 2021

@author: yan_chen
"""

import collections


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.dict[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.dict.keys():
            rest = value-num

            if rest != num:
                if rest in self.dict:
                    return True
            else:
                if self.dict[num] > 1:
                    return True
        return False
