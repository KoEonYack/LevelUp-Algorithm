"""
    @ Baek 9076 점수 집계
    @ Prob. https://www.acmicpc.net/problem/9076
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""


for i in range(int(input())):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))

    if max(arr) - min(arr) >= 4:
        print("KIN")
    else:
        print(sum(arr))

"""
4
10 8 5 7 9
10 9 10 9 5
10 3 5 9 10
1 2 3 6 9
>
24
28
KIN
KIN
"""