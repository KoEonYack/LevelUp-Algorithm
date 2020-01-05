"""
    @ Baek 11651
    @ Prob. https://www.acmicpc.net/problem/11651
      Ref.
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 01. 04
    @ End day:  20. 01. 04
"""


N = int(input())
arr = []

for _ in range(N):
    cord = list(map(int, input().split()))
    arr.append(cord)

arr.sort(key=lambda x:(x[1], x[0]))

for ele in arr:
    print(str(ele[0]) + " " + str(ele[1]))

"""
5
0 4
1 2
1 -1
2 2
3 3
>
1 -1
1 2
2 2
3 3
0 4

"""