"""
    @ Baek 9506 약수들의 합
    @ Prob. https://www.acmicpc.net/problem/9506
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

while True:
    N = int(input())
    if N == -1:
        break
    ans = []
    for i in range(1, N):
        if N % i == 0:
            ans.append(i)
    if sum(ans) == N:
        ans = [str(num) for num in ans]
        print(str(N)+" = " + " + ".join(ans))
    else:
        print(str(N)+" is NOT perfect.")

"""
6
12
28
-1
>
6 = 1 + 2 + 3
12 is NOT perfect.
28 = 1 + 2 + 4 + 7 + 14
"""