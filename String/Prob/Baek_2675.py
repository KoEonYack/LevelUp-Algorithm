"""
    @ Baek 2675
    @ Prob. https://www.acmicpc.net/problem/2675
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""


import sys

N = int(input())
for _ in range(N):
    Num, inputStr = sys.stdin.readline().split()
    print("".join([str(a) * int(Num) for a in inputStr]))


"""
2
3 ABC
5 /HTP
>
AAABBBCCC
/////HHHHHTTTTTPPPPP
"""