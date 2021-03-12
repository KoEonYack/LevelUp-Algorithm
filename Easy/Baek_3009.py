"""
    @ Baek 3009 네 번째 점
    @ Prob. https://www.acmicpc.net/problem/3009
      Ref. https://claude-u.tistory.com/170
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

arr = []
x, y = [], []

for _ in range(3):
    arr.append(list(map(int, input().split())))

for [a, b] in arr:
    if a in x:
        x.remove(a)
    else:
        x.append(a)

    if b in y:
        y.remove(b)
    else:
        y.append(b)

print(x[0], y[0])

"""
30 20
10 10
10 20
>
30 10
"""