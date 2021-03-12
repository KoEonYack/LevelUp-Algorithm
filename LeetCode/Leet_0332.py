"""
    @ LeetCode 0332. Reconstruct Itinerary
    @ Prob. https://leetcode.com/problems/reconstruct-itinerary/
      Ref.
    @ Algo: Hash + DFS
    @ Start day: 20. 10. 05.
    @ End day: 20. 10. 05.
"""

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict()
        for src, des in tickets:
            if not graph.get(src, None):
                graph[src] = [des]
            else:
                graph[src].append(des)
        
        graph = [graph[k].sort() for k in graph.keys()]
        visited = []
        def dfs(src):
            while graph.get(src, None):
                des = graph[src].pop(0)
                dfs(des)
            visited.append(src)
            
        dfs('JFK')
        return visited[::-1]
        
        
        
        
if __name__ == "__main__":
    solution = Solution()
        