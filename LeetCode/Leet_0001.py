"""
    @ 0001. Two Sum
    @ Prob. https://leetcode.com/problems/two-sum/
      Ref.
    @ Algo: Brute force
    @ Start day: 20. 07. 26.
    @ End day: 20. 07. 26.
"""

import re
import collections


class Solution(object):
    """
    @ Brute force O(n^2)
    @ 5952 ms
    """
    def twoSum_bruteforce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    """
    @ in search O(n^2)
    @ 1136ms
    """
    def twoSum_in(self, nums, target):
        for i, n in enumerate(nums):
            remain = target - n

            if remain in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(remain) + (i+1)

    """
    @ hash O(1)
    @ 40ms
    """
    def twoSum_hash(self, nums, target):
        nums_map = {}
        for i, num in enumerate(nums):
           nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return i, nums_map[target-num]



s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))