"""
    @ Baek 1764 듣보잡
    @ Prob. https://www.acmicpc.net/problem/1764
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

N, M = map(int, input().split())
A = set()
B = set()
for _ in range(N):
    A.add(input())

for _ in range(M):
    B.add(input())

set_AB = list(A & B)
print(len(set_AB))
for char in sorted(set_AB):
    print(char)


"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
>
2
baesangwook
ohhenrie
"""