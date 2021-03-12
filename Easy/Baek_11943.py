"""
    @ 백준 11943 파일 옮기기
    @ https://www.acmicpc.net/problem/11943
    @ End Day : 2020. 03. 09.
"""

A, B = map(int, input().split())
C, D = map(int, input().split())
if A + D > B + C:
    print(B+C)
else:
    print(A+D)

"""
1 2
3 4
>
5
"""