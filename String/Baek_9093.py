"""
    @ Baek 9093 단어 뒤집기
    @ Prob. https://www.acmicpc.net/problem/9093
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

N = int(input())
for _ in range(N):
    arr = list(map(str, input().split()))
    for char in arr:
        print(char[::-1], end=" ")

"""
2
I am happy today
We want to win the first prize
>
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
"""