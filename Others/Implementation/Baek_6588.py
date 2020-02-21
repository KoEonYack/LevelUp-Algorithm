"""
    @ Baek 6588 골드바흐의 추측
    @ Prob. https://www.acmicpc.net/problem/6588
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 02. 21.
    @ End day: 20. 02. 21.
"""

MAX = 1000000
check = [False] * (MAX+1)
check[0] = check[1] = True
prime = []
for i in range(2, MAX+1):
    if not check[i]:
        prime.append(i)
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i

prime = prime[1:]
while True:
    N = int(input())
    if N == 0:
        break

    for p in prime:
        if check[N-p] is False:
            print("{0} = {1} + {2}".format(N, p, N-p))
            break

"""
8
20
42
0
>
8 = 3 + 5
20 = 3 + 17
42 = 5 + 37
"""
