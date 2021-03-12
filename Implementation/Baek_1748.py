"""
    @ Baek 1748 수들의 합
    @ Prob. https://www.acmicpc.net/problem/1748
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""

N = int(input())

W = 1
ans = 0
digit_len = len(str(N))
for i in range(1, len(str(N))):
    ans += 9 * pow(10, i-1) * i

ans += (N - pow(10, digit_len - 1) + 1) * digit_len
print(ans)

"""
120
>
252

# [ check ] 
N = 50
data = ""
for i in range(1, N+1):
    data += str(i)
print(len(data))
"""
