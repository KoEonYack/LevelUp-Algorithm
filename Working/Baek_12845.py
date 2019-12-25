"""
    @ Baek 12845
    @ Prob. https://www.acmicpc.net/problem/12845
      Ref. https://m.blog.naver.com/pasdfq/221207370093
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 24.
    @ End day: 19. 12.
"""


N = int(input())
arr = list(map(int, input().split()))
levelSum = 0
maxLevelCard = 0
for i in range(N):
    levelSum += arr[i]
    maxLevelCard = max(maxLevelCard, arr[i])

print(levelSum + maxLevelCard*(N-2))


"""
3
40 30 30
"""

