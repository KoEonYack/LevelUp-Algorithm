"""
    @ Baek 10833 사과
    @ Prob. https://www.acmicpc.net/problem/10833
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

ans = 0
for i in range(int(input())):
    student, apple = map(int, input().split())
    ans += (apple % student)

print(ans)

"""
5
24 52
13 22
5 53
23 10
7 70
>
26
"""