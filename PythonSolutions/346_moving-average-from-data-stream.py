# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:07:46 2021
Given a stream of integers and a window size, calculate the moving average of 
all integers in the sliding window.

@author: yan_chen
"""


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = [0]*self.size
        self.head, self.window_sum = 0, 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head+1) % self.size
        old = self.queue[tail]
        self.window_sum = self.window_sum+val-old
        self.head = (self.head+1) % self.size
        self.queue[self.head] = val
        return self.window_sum/min(self.size, self.count)
