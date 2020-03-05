"""
    @ Baek 1408 24
    @ Prob. https://www.acmicpc.net/problem/1408
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

t = 0
while h1 != h2 or m1 != m2 or s1 != s2:
    s1 += 1
    t += 1
    if s1 == 60:
        s1 = 0
        m1 += 1
        if m1 == 60:
            m1 = 0
            h1 += 1
            if h1 == 24:
                h1 = 0

s = t % 60
m = (t // 60) % 60
h = (t // 60) // 60
print(f"{h:0>2}:{m:0>2}:{s:0>2}")


"""
13:52:30
14:00:00
>
00:07:30
"""