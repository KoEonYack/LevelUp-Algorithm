"""
    @ LeetCode 0347. Top K Frequent Elements
    @ Prob. https://leetcode.com/problems/top-k-frequent-elements/
      Ref.
    @ Algo: 
    @ Start day: 20. 10. 06.
    @ End day: 20. 10. 06.
"""

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [val[0] for i, val in enumerate(Counter(nums).most_common()) if i < k] 
        
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(nums, k))


"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
