"""
    백준 10801 카드게임
    Prob https://www.acmicpc.net/problem/10801
    End Day : 2020. 4. 14.
"""

A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = b = 0
for i in range(10):
    if A[i] > B[i]:
        a += 1
    elif A[i] < B[i]:
        b += 1

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("D")


"""
6 7 5 1 4 10 2 3 8 9
1 10 2 9 4 8 3 7 5 6
>
A
"""