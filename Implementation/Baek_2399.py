"""
    @ Baek 2399. 거리의 합
    @ Prob. https://www.acmicpc.net/problem/2399
     Ref.
    @ Algo: 구현
    @ Start day: 20. 07. 03.
    @ End day: 20. 07. 03.
"""

N = int(input())
lst = list(map(int, input().split()))
print(lst)

ans = 0
for i in range(N):
    for j in range(N):
        ans += abs(lst[i] - lst[j])
print(ans)

"""
5
1 5 3 2 4
>
40
"""