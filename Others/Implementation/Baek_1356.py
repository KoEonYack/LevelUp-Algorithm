"""
    @ Baek 1365 유진수
    @ Prob. https://www.acmicpc.net/problem/1365
      Ref.
    @ Algo: 구현
    @ Start day: 20. 07. 20.
    @ End day: 20. 07. 20.
"""

def multi(val):
    res = 1
    for num in val:
        res *= int(num)
    return res


input_s = input()
ans = "NO"
if len(input_s) == 1:
    print(ans)
else:
    for i in range(1, len(input_s)):
        if multi(input_s[:i]) == multi(input_s[i:]):
            ans = "YES"
            break
    print(ans)

    # print(input_s[:i], input_s[i:])