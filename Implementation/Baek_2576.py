"""
    @ Baek 2576 홀수
    @ Prob. https://www.acmicpc.net/problem/2576
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

arr = [int(input()) for _ in range(7)]
ans = []
for num in arr:
    if num % 2 == 1:
        ans.append(num)

if len(ans) != 0:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)

"""
12
77
38
41
53
92
85
>
256
41
"""