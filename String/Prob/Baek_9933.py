"""
    @ Baek 9933 민균이의 비밀번호
    @ Prob. https://www.acmicpc.net/problem/9933
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 04. 19.
    @ End day: 20. 04. 19.
"""

words = []
for i in range(int(input())):
    words.append(input())
for word in words:
    if word[::-1] in words:
        print(len(word), word[int(len(word) / 2)])
        break

"""
4
las
god
psala
sal
>
3 a
"""