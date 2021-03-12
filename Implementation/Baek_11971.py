"""
    @ Baek 11971 속도 위반
    @ Prob. https://www.acmicpc.net/problem/11971
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

N, M = map(int, input().split())
road = []

for i in range(N):
    r, speed = map(int, input().split())
    road += [speed] * r

ans = 0
end = 0
for j in range(M):
    a, b = map(int, input().split())
    for k in range(end, end+a):
        if road[k] < b:
            ans = max(ans, b-road[k])
    end += a

print(ans)


"""
3 3
40 75
50 35
10 45
40 76
20 30
40 40
>
5
"""