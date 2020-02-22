"""
    @ 1107. 크게 만들기
    @ Prob. https://www.acmicpc.net/problem/2812
     Ref.
    @ Algo: B
    @ Start day: 20. 02. 02.
    @ End day: 20. 02. 02.
"""

from itertools import product


def makeDigit(arr):
    ans = 0
    digit = 1
    for num in arr[::-1]:
        ans = ans + num * digit
        digit *= 10

    return ans


N = int(input())
M = int(input())
ban_num_arr = list(map(int, input().split()))
ans_digit_len = len(str(N))
candidate_num_arr = [i for i in range(0, 10)]

for i in range(M):
    candidate_num_arr.remove(ban_num_arr[i])

#permutationList = list(permutations(candidate_num_arr, 4))

semi_digit = 500001
diff = 500001

for arr in list(product(candidate_num_arr, repeat=N)):
    permuation_digit = makeDigit(arr)
    if diff > abs(N - permuation_digit):
        diff = abs(N - permuation_digit)
        semi_digit = permuation_digit

print(semi_digit, ans_digit_len)
print(ans_digit_len + abs(semi_digit - N))

"""
5457
3
6 7 8
>
6
-------------------
500000
8
0 2 3 4 6 7 8 9
>
11117
"""