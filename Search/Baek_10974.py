"""
    @ Baek 10974 모든 순열
    @ Prob. https://www.acmicpc.net/problem/10974
      Ref.
      Ref Prob.
    @ Algo: Brute-force
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""


def permutaions(selected, k):
    if k == N:
        print(*selected)
    else:
        for i in range(1, N+1):
            if i not in selected:
                permutaions(selected+[i], k+1)


N = int(input())
permutaions([], 0)
print("END")


"""
3
>
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

