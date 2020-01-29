"""
    @ Baek 2231 분해합
    @ Prob. https://www.acmicpc.net/problem/2231
      Ref.
      Ref Prob.
    @ Algo: Brute-force
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

N = int(input())
print_num = 0
for i in range(1, N+1):
    div_num_arr = list(map(int, str(i)))
    res = sum(div_num_arr) + i
    if res == N:
        print_num = i
        break

print(print_num)

"""
216
>
198
"""