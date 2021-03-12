"""
    @ Baek 4592 중복을 없애자
    @ Prob. https://www.acmicpc.net/problem/4592
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

while True:
    N, *arr = map(int, input().split())
    if N == 0:
        break
    print(arr[0], end=" ")
    for i in range(1, N):
        if arr[i-1] == arr[i]:
            continue
        else:
            print(arr[i], end=" ")
    print("$")

"""
5 1 22 22 22 3
4 98 76 20 76
6 19 19 35 86 86 86
1 7
0
>
1 22 3 $
98 76 20 76 $
19 35 86 $
7 $
"""