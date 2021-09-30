# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:33:23 2021

@author: yan_chen
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Time: O(k*2^N)
        # Space: O(N)

        n = len(nums)
        nums.sort(reverse=True)
        targetSum, remain = divmod(sum(nums), k)
        if n < k or nums[0] > targetSum or remain != 0:
            return False

        taken = [False]*n

        def backtrack(index, count, currSum):
            if count == k-1:
                return True

            if currSum > targetSum:
                return False

            if currSum == targetSum:
                return backtrack(0, count+1, 0)

            for i in range(index, n):
                if not taken[i]:
                    taken[i] = True

                    if backtrack(i+1, count, currSum+nums[i]):
                        return True

                    taken[i] = False
            return False

        return backtrack(0, 0, 0)
