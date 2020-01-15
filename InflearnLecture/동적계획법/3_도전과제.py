"""
    @ 3. 도전과제
    @ Start day: 20. 01. 15
    @ End day: 20. 01. 15
"""


def DFS(Num):
    if D[Num] > 0:
        return D[Num]
    if Num == 1 or Num == 2:
        return Num
    else:
        D[Num] = DFS(Num-1) + DFS(Num-2)
        return D[Num]


N = int(input())
D = [0] * (N+1)
print(DFS(N))


"""
7
>
21
"""