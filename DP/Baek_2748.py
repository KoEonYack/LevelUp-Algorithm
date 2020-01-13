"""
    @ 2748. 피보나치 수 2
    @ Prob. https://www.acmicpc.net/problem/2748
     Ref.
    @ Algo: Recursion
    @ Start day: 20. 01. 12.
    @ End day: 20. 01. 12.
"""


N = int(input())
D = [0, 1]

for i in range(2, N + 1):
    D.append(D[i-2] + D[i-1])

print(D[N])


"""
10
>
55
"""