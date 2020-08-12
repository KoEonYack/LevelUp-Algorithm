"""
    @ 0001. Two Sum
    @ Prob. https://leetcode.com/problems/letter-combinations-of-a-phone-number/
      Ref.
    @ Algo: Brute force
    @ Start day: 20. 08. 12.
    @ End day: 20. 08. 12.
"""


class Solution:
        
    def letterCombinations(self, digits: str):
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def dfs(idx, path):
            if len(path) == len(digits):
                res.append(path)
                return 
            
            for i in range(idx, len(digits)):
                for dig in dic[digits[i]]:
                    dfs(i+1, path + dig)
        
        if not digits:
            return []
        
        dfs(0, "")

        return res

s = Solution()
digits = "23"
print(s.letterCombinations(digits))

"""
23
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

