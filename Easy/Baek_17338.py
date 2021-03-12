"""
    @ 백준 17388 와글와글 숭고한
    @ https://www.acmicpc.net/problem/17338
    @ End Day : 2020. 01. 29.
"""

# S + K + H
arr = list(map(int, input().split()))
if sum(arr) >= 100:
    print("OK")
elif min(arr) == arr[0]:
    print("Soongsil")
elif min(arr) == arr[1]:
    print("Korea")
elif min(arr) == arr[2]:
    print("Hanyang")


"""
45 33 21
>
Hanyang
"""