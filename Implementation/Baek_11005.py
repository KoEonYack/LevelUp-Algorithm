"""
    @ Baek 11005 진법 변환 2
    @ Prob. https://www.acmicpc.net/problem/11005
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, input().split())
ans = ""
while N != 0:
    ans += data[N%B]
    N = N // B
print(ans[::-1])

"""
60466175 36
>
ZZZZZ
"""

