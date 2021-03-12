"""
    @ Baek 2822 점수 계산
    @ Prob. https://www.acmicpc.net/problem/2822
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

import sys

arr = []
ans = []
for _ in range(8):
    arr.append(int(sys.stdin.readline()))

new_arr = sorted(arr, reverse=True)[0:5]

print(sum(new_arr))
for i in range(5):
    ans.append(arr.index(new_arr[i]) + 1)

ans.sort()
for i in range(5):
    print(ans[i], end=" ")


"""
20
30
50
48
33
66
0
64
>
261
3 4 5 6 8
"""