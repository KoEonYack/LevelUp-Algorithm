"""
    @ Baek 6209 제자리 멀리뛰기
    @ Prob. https://www.acmicpc.net/problem/6209
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 20. 04. 02.
    @ End day: 20. 04. 02.
"""

def check(x):
    cnt = 0
    cur = S[0]

    for i in range(1, N+2):
        if S[i] < cur + x: cnt += 1
        else: cur = S[i]

    return cnt <= M and cur == D

lb = 0
ub = 1000000000
L = 0
D, N, M = map(int, input().split())
S = [int(input()) for _ in range(N)]
S.append(0)
S.append(D)
S.sort()
print(S)
while lb < ub:
    L = (lb + ub + 1) // 2
    if check(L): lb = L
    else: ub = L - 1

print(ub)


"""
25 5 2
2
14
11
21
17
>
4
"""