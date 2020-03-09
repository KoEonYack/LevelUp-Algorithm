"""
    @ 백준 10101 삼각형 외우기
    @ https://www.acmicpc.net/problem/10101
    @ End Day : 2020. 03. 09.
"""

arr = [int(input()) for _ in range(3)]

if sum(arr) == 180:
    if arr[0] == arr[1] == arr[2] == 60:
        print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        print("Isosceles")
    elif arr[0] != arr[1] != arr[2]:
        print("Scalene")
else:
    print("Error")