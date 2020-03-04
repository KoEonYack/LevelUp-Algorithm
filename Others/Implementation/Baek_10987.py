"""
    @ Baek 10987 모음의 개수
    @ Prob. https://www.acmicpc.net/problem/10987
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

inputStr = input()
ans = 0
for ch in inputStr:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        ans += 1

print(ans)


"""
baekjoon
>
4
"""