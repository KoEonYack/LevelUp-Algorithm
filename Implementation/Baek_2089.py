"""
    @ Baek 2089 -2진수
    @ Prob. https://www.acmicpc.net/problem/2089
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 02. 21.
    @ End day: 20. 02. 21.
"""

N = int(input())
base = 1
st = []

if N == 0:
    print(0)
else:
    while N:
        if N % 2:
            st.append(1)
            N -= base
        else:
            st.append(0)
        base *= (-1)
        N //= 2

for num in st[::-1]:
    print(num, end="")


"""
-13
>
110111
"""