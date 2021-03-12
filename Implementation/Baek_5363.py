"""
    @ Baek 5363 요다
    @ Prob. https://www.acmicpc.net/problem/5363
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

for _ in range(int(input())):
    arr = list(map(str, input().split()))
    print(" ".join(arr[2:]) + " " + " ".join(arr[0:2]))

"""
4
I will go now to find the Wookiee
Solo found the death star near planet Kessel
I'll fight Darth Maul here and now
Vader will find Luke before he can escape
>
go now to find the Wookiee I will
the death star near planet Kessel Solo found
Darth Maul here and now I'll fight
find Luke before he can escape Vader will
"""