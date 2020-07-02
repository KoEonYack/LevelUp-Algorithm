"""
    @ Baek 15904. UCPC는 무엇의 약자일까?
    @ Prob. https://www.acmicpc.net/problem/15904
     Ref.
    @ Algo: Implement
    @ Start day: 20. 07. 02.
    @ End day: 20. 07. 02.
"""

S = input()
res = ""
data = ["U", "C", "P", "C"]
idx = 0

for ch in S:
    if ch == data[idx]:
        idx += 1

    if idx == 4:
        break

if idx == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")


"""
Union of Computer Programming Contest club contest
>
I love UCPC

University Computer Programming
>
I hate UCPC
"""