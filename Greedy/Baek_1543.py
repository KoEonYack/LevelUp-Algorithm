"""
    @ Baek 1543. 문서 검색
    @ Prob. https://www.acmicpc.net/problem/1543
     Ref.   
    @ Algo: Greedy - Fail
    @ Start day: 20. 08. 27. 
    @ End day: 20. 08. 27.
"""


string = input()
search = input()

idx = 0
ans = 0
for ch in string:
    if ch == search[idx]:
        idx += 1
        if idx == len(search):
            ans += 1
            idx = 0
    else:
        idx = 0

print(ans)


"""
ababababa
aba
>
2
----------
a a a a a
a a
>
2
"""