"""
    @ Baek 1764. 듣보잡
    @ Prob. https://www.acmicpc.net/problem/1764
     Ref.
    @ Algo: Tree
    @ Start day: 20. 03. 26.
    @ End day: 20. 03 26.
"""

s1, s2 = set(), set()
N, M = map(int, input().split())
for _ in range(N):
    s1.add(input())
for _ in range(M):
    s2.add(input())

l = list(s1 & s2)
print(len(l))
print("\n".join(sorted(l)))

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