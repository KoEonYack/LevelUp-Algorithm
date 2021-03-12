"""
    @ Baek 11425 문자열 집합
    @ Prob. https://www.acmicpc.net/problem/11425
      Ref.  
    @ Algo: sbin 
    @ Start day: 20. 09. 16.
    @ End day: 20. 09. 16.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {input().rstrip() for _ in range(N)}

cnt = 0
for i in range(M):
    CHK = input().rstrip()
    if CHK in S:
        cnt += 1
print(cnt)
    


"""
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
>
4
"""



