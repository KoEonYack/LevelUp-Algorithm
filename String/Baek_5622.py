"""
    @ Baek 5622 다이얼
    @ Prob. https://www.acmicpc.net/problem/5622
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

inputStr = input()
ans = 0
for char in inputStr:
    if char in ['A', 'B', 'C']:
        ans += 3
    elif char in ['D', 'E', 'F']:
        ans += 4
    elif char in ['G', 'H', 'I']:
        ans += 5
    elif char in ['J', 'K', "L"]:
        ans += 6
    elif char in ['M', 'N', 'O']:
        ans += 7
    elif char in ['P', 'Q', 'R', 'S']:
        ans += 8
    elif char in ['T', 'U', 'V']:
        ans += 9
    elif char in ['W', 'X', 'Y', 'Z']:
        ans += 10

print(ans)


"""
UNUCIC
>
36

"""