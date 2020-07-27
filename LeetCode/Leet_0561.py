"""
    @ Leet 0561. Array Partition I
    @ Prob. https://leetcode.com/problems/array-partition-i/
      Ref.
    @ Algo: Stack
    @ Start day: 20. 07. 27.
    @ End day: 20. 07. 27.
"""

class Solution:

    def arrayPairSum_bruteforce(self, nums) -> int:
        ans = 0
        pair = []
        nums.sort()
        for num in nums:
            pair.append(num)
            if len(pair) % 2 == 0:
                ans += min(pair)
                pair = []

        return ans

    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


s = Solution()
nums = [1,4,3,2]
print(s.arrayPairSum(nums))