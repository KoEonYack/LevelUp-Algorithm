"""
    @ Baek 8976 올림픽
    @ Prob. https://www.acmicpc.net/problem/8976
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""


N, Nation = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)
print(arr)


