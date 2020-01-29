"""
    @ Baek 11728 배열 합치기
    @ Prob. https://www.acmicpc.net/problem/11728
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(*sorted(list((arr1 + arr2))))


"""
2 2
3 5
2 9
>
2 3 5 9

2 1
4 7
1
>
1 4 7

4 3
2 3 5 9
1 4 7
>
1 2 3 4 5 7 9
"""