"""
    @ Baek 10814
    @ Prob. https://www.acmicpc.net/problem/10814
      Ref.
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 01. 04
    @ End day:  20. 01. 04
"""

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(str, input().split())))

arr.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(arr[i][0], arr[i][1])


"""
3
21 Junkyu
21 Dohyun
20 Sunyoung

>

20 Sunyoung
21 Junkyu
21 Dohyun
"""