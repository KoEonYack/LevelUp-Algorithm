"""
    @ Leet 1422. Maximum Score After Splitting a String
    @ Prob. https://leetcode.com/problems/maximum-score-after-splitting-a-string/
     Ref.
    @ Algo: 구현
    @ Start day: 20. 05. 01.
    @ End day: 20. 05. 01.
"""

"""
number of zeros in the left substring plus 
the number of ones in the right substring.
"""
def maxScore(s):
    """
    :type s: str
    :rtype: int
    """
    ans = 0
    for i in range(1, len(s)):
        left = s[:i].count("0")
        right = s[i:].count("1")
        if left + right > ans:
            ans = left + right
        # print(left, right)

    return ans

print(maxScore("011101"))
print(maxScore("00111"))
print(maxScore("1111"))
