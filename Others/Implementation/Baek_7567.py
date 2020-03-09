"""
    @ Baek 7567 그릇
    @ Prob. https://www.acmicpc.net/problem/7567
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

s = input()
ans = 10
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        ans += 10
    else:
        ans += 5
print(ans)


"""
((((
>
25
"""