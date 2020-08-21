"""
    @ Leet 0039.Combination Sum
    @ Prob. https://leetcode.com/problems/combination-sum/
      Ref.
    @ Algo: DFS
    @ Start day: 20. 08. 13.
    @ End day: 20. 08. 13.
"""

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def dfs(total, idx, path):
            if total < 0: return
            elif total == 0:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                dfs(total - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return res

s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates, target))