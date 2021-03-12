"""
    @ Baek 5347 LCM
    @ Prob. https://www.acmicpc.net/problem/5347
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

for _ in range(int(input())):
    arr = list(map(str, input().split()))
    arr[0] = float(arr[0])
    for ch in arr[1:]:
        if ch == "@":
            arr[0] *= 3
        elif ch == "%":
            arr[0] += 5
        elif ch == "#":
            arr[0] -= 7
    print("%.2f"%arr[0])


"""
3
3 @ %
10.4 # % @
8 #
>
14.00
25.20
1.00
"""