"""
    @ Baek 1547 공
    @ Prob. https://www.acmicpc.net/problem/1547
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

arr = [0, 1, 0, 0]
for _ in range(int(input())):
    x, y = map(int, input().split())
    if arr[x] == 1:
        arr[y] = 1
        arr[x] = 0
    elif arr[y] == 1:
        arr[y] = 0
        arr[x] = 1

print(arr.index(1))


"""
4
3 1
2 3
3 1
3 2
>
3
"""