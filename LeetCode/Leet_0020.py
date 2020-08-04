"""
    @ Leet 0020.Valid Parentheses
    @ Prob. https://leetcode.com/problems/valid-parentheses/
      Ref.
    @ Algo: Stack
    @ Start day: 20. 08. 04.
    @ End day: 20. 08. 04.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c not in table:
                stack.append(c)
            # stack 비어있거나, 시작괄호 쌍이 안 맞는 경우
            elif not stack or table[c] != stack.pop():
                return False

        return len(stack) == 0

s = Solution()
inputS = "()[]{}"
inputS = "]"
print(s.isValid(inputS))
