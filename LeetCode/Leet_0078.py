"""
    @ Leet 0078.Subsets
    @ Prob. https://leetcode.com/problems/subsets/
      Ref.
    @ Algo: DFS
    @ Start day: 20. 08. 18.
    @ End day: 20. 08. 18.
"""


class Solution:
    def subsets(self, nums):
        result = []

        def DFS(idx, path):
            result.append(path)

            for i in range(idx, len(nums)):
                DFS(i+1, path + [nums[i]])

        DFS(0, [])
        return result


nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))