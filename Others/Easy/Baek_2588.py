"""
    백준 2588번 곱셈
    Prob https://www.acmicpc.net/problem/2588
    End Day : 2020. 1. 1
"""

A = int(input())
B = int(input())
arr_B = [int(i) for i in str(B)]
arr_B.reverse()

for i in range(len(arr_B)):
    print(A * arr_B[i])
print(A * B)

"""
472
385

>>
2360
3776
1416
181720
"""