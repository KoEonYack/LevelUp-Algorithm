"""
    @ Baek 5597 과제 안 내신 분..?
    @ Prob. https://www.acmicpc.net/problem/5597
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

import sys

arr = [(i+1) for i in range(30)]
for i in range(1, 29):
    arr.remove(int(sys.stdin.readline()))

print(str(arr[0]) + "\n" + str(arr[1]))

"""
3
1
4
5
7
9
6
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
>
2
8
"""


