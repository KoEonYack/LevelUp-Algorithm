"""
    @ 15989. 1, 2, 3 더하기 4
    @ Prob. https://www.acmicpc.net/problem/15989
      Ref.
    @ Algo: DP
    @ Start day: 20. 03. 10.
    @ End day: 20. 03. 10.
"""

nums = [1, 2, 3]
MAX_SIZE = 100001
DP = [0] * MAX_SIZE
DP[0] = 1
for j in range(0, 3):
    for i in range(1, MAX_SIZE):
        if i - nums[j] >= 0:
            DP[i] += DP[i-nums[j]]

#print(DP)
for _ in range(int(input())):
    print(DP[int(input())])

"""
3
4
7
10
>
4
8
14
"""

