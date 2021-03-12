"""
    @ Baek 2010 플러그
    @ Prob. https://www.acmicpc.net/problem/2010
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

total_sum = 0
N = int(input())
for i in range(N):
    total_sum += int(input())
print(total_sum - (N-1))

"""
3
1
1
1
>
1
"""