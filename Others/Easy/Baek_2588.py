"""
    백준 2588번 곱셈
    Prob https://www.acmicpc.net/problem/2588
    End Day : 2020. 1. 1
"""

A = int(input())
B = int(input())
intList_B = [int(i) for i in str(B)]
intList_B.reverse()

for i in range(len(intList_B)):
    print(A * intList_B[i])
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