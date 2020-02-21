"""
    @ Baek 1929 소수 구하기
    @ Prob. https://www.acmicpc.net/problem/1934
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""

MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True

for i in range(2, MAX+1):
    if not check[i]:
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i

M, N = map(int, input().split())
for i in range(M, N+1):
    if check[i] == False:
        print(i)


"""
3 16
>
3
5
7
11
13
"""