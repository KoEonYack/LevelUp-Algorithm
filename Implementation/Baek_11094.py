"""
    @ Baek 11094 꿍 가라사대
    @ Prob. https://www.acmicpc.net/problem/11094
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 06. 07.
    @ End day: 20. 06. 07.
"""

N = int(input())
for i in range(N):
    A = input()
    S = A.split()
    if S[0] == "Simon" and S[1] == "says":
        print(A[10:])



"""
1
Simon says smile.
>
smile.
"""

