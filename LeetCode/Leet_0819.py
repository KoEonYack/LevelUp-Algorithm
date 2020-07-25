"""
    @ 819. Most Common Word
    @ Prob. https://leetcode.com/problems/most-common-word/
      Ref.
    @ Algo: String
    @ Start day: 20. 07. 25.
    @ End day: 20. 07. 25.
"""

import re
import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = [word for word in re.sub(r'[^\w]', " ", paragraph)
                 .lower().split()
                 if word not in banned]
        return collections.Counter(words).most_common(1)[0][0]

s = Solution()
p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
print(s.mostCommonWord(p, b))