"""
    @ Baek 8976 올림픽
    @ Prob. https://www.acmicpc.net/problem/8976
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 14
    @ End day: 20. 01. 14
"""

import sys

N, K = map(int, input().split())
country = []

for i in range(N):
    country.append(list(map(int, input().split())))
country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

idx = [country[i][0] for i in range(N)].index(K)

while country[idx-1][1:] == country[idx][1:] and idx >= 1:
    idx -= 1

print(idx+1)


"""
4 3
1 1 0 0 
2 1 0 0
3 1 0 0
4 1 0 0
1 1 1 1

>
2
"""