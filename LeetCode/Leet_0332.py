"""
    @ Leet 0332. reconstruct itinerary
    @ Prob. https://leetcode.com/problems/reconstruct-itinerary/solution/
      Ref.
    @ Algo: Stack
    @ Start day: 20. 08. 19.
    @ End day: 20. 08. 19.
"""

from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        # print(sorted(tickets))
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def DFS(a):
            while graph[a]:
                DFS(graph[a].pop(0))
            print(a)
            route.append(a)

        DFS('JFK')
        return route[::-1]


s = Solution()

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"]]

# sorted([["A", "A"], ["A", "B"])
# sorted([["A", "B"], ["A", "A"])

print(s.findItinerary(tickets))

"""
[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
> ["JFK", "MUC", "LHR", "SFO", "SJC"]
"""