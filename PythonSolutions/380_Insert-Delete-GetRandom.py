# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:17:17 2021

@author: yan_chen
"""
import random


class RandomizedSet:

    def __init__(self):

        self.nums = []
        self.dict = {}

    def insert(self, val: int) -> bool:

        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:

        if val not in self.dict:
            return False
        else:
            lastVal, index = self.nums[-1], self.dict[val]
            self.nums[index] = lastVal
            self.nums.pop()
            self.dict[lastVal] = index
            del self.dict[val]
            return True

    def getRandom(self) -> int:

        return random.choice(self.nums)
