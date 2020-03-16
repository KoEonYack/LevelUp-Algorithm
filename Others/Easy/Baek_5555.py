"""
    @ Baek 5555 반지
    @ Prob. https://www.acmicpc.net/problem/5555
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

pattern = input()
ans = 0
for _ in range(int(input())):
    target = input()
    if pattern in target*2:
        ans += 1
print(ans)



"""
ABCD
3
ABCDXXXXXX
YYYYABCDXX
DCBAZZZZZZ
>
2
--------------
XYZ
1
ZAAAAAAAXY
>
1


"""
