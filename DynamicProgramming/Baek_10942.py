"""
    @ 10942. 팰린드롬?
    @ Prob. https://www.acmicpc.net/problem/10942
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 28.
    @ End day: 20. 02. 28.
"""
N = int(input())
A = [0] + list(map(int, input().split()))
DP = [[False] * (N + 4) for _ in range(N+4)]

for i in range(1, N+1):
    DP[i][i] = True

for i in range(1, N):
    if A[i] == A[i+1]:
        DP[i][i+1] = True

for i in range(len(A)-1, 0, -1):
    for j in range(i+1, len(A)):
        #print(i, j, A[i], A[j], DP[i+1][j])
        if A[i] == A[j] and DP[i+1][j-1] is True:
            DP[i][j] = True


#for a in DP:
#    print(a)

for _ in range(int(input())):
    X, Y = map(int, input().split())
    if DP[X][Y] == True:
        print(1)
    else:
        print(0)

"""
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
>
1
0
1
1
-----------
"""