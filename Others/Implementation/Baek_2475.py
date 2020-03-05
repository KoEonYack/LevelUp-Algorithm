"""
    @ Baek 2475 검증수
    @ Prob. https://www.acmicpc.net/problem/2475
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

arr = list(map(int, input().split()))
ans = 0
for num in arr:
    ans += pow(num, 2)
print(ans % 10)

"""
0 4 2 5 6
>
1
"""