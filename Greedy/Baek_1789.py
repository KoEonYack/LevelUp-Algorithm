"""
    @ Baek 1789. 수들의 합
    @ Prob. https://www.acmicpc.net/problem/1789
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 05.
    @ End day: 20. 02. 05.
"""

Target = int(input())

i = 0
curr = 0
while True:
    i += 1
    curr += i
    if curr > Target: break

print(i-1)


"""
200
>
19
"""