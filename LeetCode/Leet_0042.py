"""
    @ 0042. Trapping Rain Water
    @ Prob. https://leetcode.com/problems/trapping-rain-water/
      Ref.
    @ Algo: Stack
    @ Start day: 20. 07. 27.
    @ End day: 20. 07. 27.
"""


class Solution:
    def trap(self, height) -> int:
        stack = []

        for i in range(len(height)):
            pass


s = Solution()
nums = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(nums))