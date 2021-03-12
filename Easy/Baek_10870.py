"""
    백준 10870 피보나치 수 5
    End Day : 2020. 1. 2
"""

import sys
sys.setrecursionlimit(100000)

def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        fibo(N-1) + fibo(N-2)


inputN = int(input())
print(fibo(inputN))