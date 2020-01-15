"""
Note.
    DFS(7): 7m를 1,2m로 자르는 방법을 리턴

    @ 2. 네트워크 선자르기(Top-Down)
    @ Start day: 20. 01. 15
    @ End day: 20. 01. 15
"""


def DFS(Num):
    if D[Num] > 0:
        return D[Num]

    if Num == 1 or Num == 2:
        return Num
    else:
        D[Num] = DFS(Num - 1) + DFS(Num - 2)
        return D[Num]


N = int(input())
D = [0] * (N+1)
print(DFS(N))
print(D)

"""
7
45

>
1836311903  
"""