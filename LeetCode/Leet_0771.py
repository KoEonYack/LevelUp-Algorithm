"""
    @ Leet 0771. Jewels and Stones
    @ Prob. https://leetcode.com/problems/jewels-and-stones/
      Ref.
    @ Algo: Stack
    @ Start day: 20. 08. 04.
    @ End day: 20. 08. 04.
"""

from collections import defaultdict
from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq = defaultdict(int)
        for s in S:
            freq[s] += 1

        ans = 0
        for j in J:
            ans += freq[j]

        return ans

    def numJewelsInStonesV2(self, J: str, S: str) -> int:
        freq = Counter(S)

        ans = 0
        for j in J:
            ans += freq[j]
        return ans

    def numJewelsInStonesV3(self, J: str, S: str) -> int:
        return sum(s in J for s in S )


s = Solution()
J = "aA"
S = "aAAbbbb"
print(s.numJewelsInStones(J, S))
print(s.numJewelsInStonesV2(J, S))