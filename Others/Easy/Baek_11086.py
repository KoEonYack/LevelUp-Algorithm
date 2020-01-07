"""
    @ Baek 10886 0 = not cute / 1 = cute
    @ Prob. https://www.acmicpc.net/problem/10886
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

import sys

cute = 0
not_cute = 0
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 1:
        cute += 1
    else:
        not_cute += 1

print("Junhee is cute!" if cute > not_cute else "Junhee is not cute!")

"""
3
1
0
0
>
Junhee is not cute!
or
Junhee is cute!
"""
