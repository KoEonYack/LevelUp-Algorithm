"""
    @ Baek 10826 피보나치 수 4
    @ Prob. https://www.acmicpc.net/problem/10826
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

N = int(input())
fibo = [0, 1, 1]
for i in range(3, N+1):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[N])


"""
10
>
55
"""