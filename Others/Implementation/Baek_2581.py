"""
    @ Baek 2581 소수
    @ Prob. https://www.acmicpc.net/problem/2581
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

MAX_SIZE = 10000
check = [False, False] + [True] * (MAX_SIZE)
primes = []
prime_count = 0

for i in range(1, len(check)):
    if check[i]:
        primes.append(i)
        for j in range(i*2, len(check), i):
            check[j] = False

M = int(input())
N = int(input())

ans = []
for prime in primes:
    if M <= prime <= N:
        ans.append(prime)
    if prime > N:
        break

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))


"""
60
100
>
620
61
"""