"""
    @ Baek 1919 애너그램 만들기
    @ Prob. https://www.acmicpc.net/problem/1919
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 12.
    @ End day: 20. 04. 12.
"""

alpha1 = [0] * 27
alpha2 = [0] * 27

str1 = input()
str2 = input()
for i in range(ord('a'), ord('z')+1):
    alpha1[i-ord('a')] = str1.count(chr(i))
    alpha2[i-ord('a')] = str2.count(chr(i))

res = 0
for i in range(27):
    if alpha1[i] != alpha2[i]:
        res += abs(alpha1[i] - alpha2[i])

print(res)

"""
aaa
aaa

aabbcc
xxyybb
>
8
"""

