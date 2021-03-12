"""
    @ Baek 9613 GCD 합
    @ Prob. https://www.acmicpc.net/problem/9613
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""

from math import gcd
from itertools import combinations

for i in range(int(input())):
    ans = 0
    N, *inputArr = map(int, input().split())
    iterArr = [i for i in range(N)]
#    print(list(combinations(iterArr, 2)))
    for ele in list(combinations(iterArr, 2)):
        ans += gcd(inputArr[ele[0]], inputArr[ele[1]])
    print(ans)


"""
3
4 10 20 30 40
3 7 5 12
3 125 15 25
>
70
3
35
"""