"""
    @ Baek 5176 대회 자리
    @ Prob. https://www.acmicpc.net/problem/5176
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 06.
    @ End day: 20. 03. 06.
"""

for _ in range(int(input())):
    P, M = map(int, input().split())
    arr = []
    for _ in range(P):
        arr.append(int(input()))
    print(P - len(set(arr)))


"""
3
4 1
1
1
1
1
4 4
1
2
3
4
4 4
1
4
1
4
>>>>>>>>>>>>>>>
3
0
2
"""