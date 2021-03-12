"""
    @ Baek 2506 점수계산
    @ Prob. https://www.acmicpc.net/problem/2506
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

N = int(input())
arr = list(map(int, input().split()))
ans = 0
cul = 1

for num in arr:
    if num == 1:
        ans += cul
        cul += 1
    else:
        cul = 1

print(ans)

"""
10
1 0 1 1 1 0 0 1 1 0
>
10
"""