"""
    @ LeetCode 122. Best Time to Buy and Sell Stock II
    @ Prob. https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
      Ref.  https://somjang.tistory.com/entry/leetCode-121-Best-Time-to-Buy-and-Sell-Stock-Python
    @ Algo: 
    @ Start day: 20. 10. 08.
    @ End day: 20. 10. 08.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

    
class SolutionSecond(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    k = 7
    solution = Solution()
    print(solution.maxProfit(nums))


