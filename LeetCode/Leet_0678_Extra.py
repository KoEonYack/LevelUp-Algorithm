"""
    @ Leet 0678.Valid Parenthesis String
    @ Prob. https://leetcode.com/problems/valid-parenthesis-string/
      Ref.
    @ Algo: Stack
    @ Start day: 20. 08. 04.
    @ End day: 20. 08. 04.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c not in table:
                stack.append(c)



s = Solution()
inputS = "(*))"
print(s.checkValidString(inputS))
