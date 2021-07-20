# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:01:37 2021

@author: yan_chen
"""


class Solution:
    def merge_sort(self, nums):

        # bottom cases: empty or list of a single element.
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        left_list = self.merge_sort(nums[:pivot])
        right_list = self.merge_sort(nums[pivot:])
        return self.merge(left_list, right_list)

    def merge(self, left_list, right_list):
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1

        # append what is remained in either of the lists
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])

        return ret

    def quick_sort(self, nums):
        def partition(nums, lo, hi):
            pivot = nums[hi]
            i = lo
            for j in range(lo, hi):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[hi] = nums[hi], nums[i]
            return i

        def sort(nums, lo, hi):
            if lo < hi:
                p = partition(nums, lo, hi)
                sort(nums, lo, p-1)
                sort(nums, p+1, hi)

        sort(nums, 0, len(nums)-1)
        return nums


Test = Solution()

nums = [5, 1, 1, 2, 0, 0]

print(Test.quick_sort(nums))
