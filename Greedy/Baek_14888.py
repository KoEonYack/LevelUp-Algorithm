"""
    @ Baek 14888. 연산자 끼워넣기
    @ Prob. https://www.acmicpc.net/problem/14888
     Ref.   
    @ Algo: Greedy
    @ Start day: 20. 08. 26.
    @ End day: 20. 08. 26.
"""


import sys


def cal(res, idx, add, sub, mul, div):
    global maxV, minV
    
    if idx == N:
        maxV = max(res, maxV)
        minV = min(res, minV)
        return 
    else:
        if add:
            cal(res+arr[idx], idx+1, add-1, sub, mul, div)
        if sub:
            cal(res-arr[idx], idx+1, add, sub-1, mul, div)
        if mul:
            cal(res*arr[idx], idx+1, add, sub, mul-1, div)
        if div:
            cal(int(res/arr[idx]), idx+1, add, sub, mul, div-1)

maxV = -sys.maxsize
minV = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
cal(arr[0], 1, a, b, c, d)
print(maxV)
print(minV)


"""
2
5 6
0 0 1 0
>
30
30

------------------

6
1 2 3 4 5 6
2 1 1 1
>
54
-24

"""






