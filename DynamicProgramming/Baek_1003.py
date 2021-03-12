"""
    @ 1003. 피보나치 함수
    @ Prob. https://www.acmicpc.net/problem/1003
     Ref.   https://hongku.tistory.com/164
    @ Algo: Recursion
    @ Start day: 20. 01. 12.
    @ End day: 20. 01. 12.
"""

N = int(input())
D = [0, 1]

for i in range(2, N + 1):
    D.append(D[i-2] + D[i-1])

for _ in range(N):
    num = int(input())
    if num == 0:
        print("1 0")
    elif num == 1:
        print("0 1")
    else:
        print(D[num-1], D[num])


"""
3
0
1
3
>
1 0
0 1
1 2
"""