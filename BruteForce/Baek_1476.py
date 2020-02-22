"""
    @ 1476. 날짜 계산
    @ Prob. https://www.acmicpc.net/problem/1476
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 02. 22.
    @ End day: 20. 02. 22.
"""


E, S, M = map(int, input().split())
# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

e = s = m = 1
year = 1
while True:
    if e == E and s == S and m == M:
        print(year)
        break
    else:
        e += 1
        s += 1
        m += 1
        year += 1
        if e >= 16:
            e = 1
        if s >= 29:
            s = 1
        if m >= 20:
            m = 1

"""
15 28 19
>
7980
"""