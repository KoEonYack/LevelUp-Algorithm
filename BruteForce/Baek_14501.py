"""
    @ 14501. 퇴사
    @ Prob. https://www.acmicpc.net/problem/14501
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 02. 24.
    @ End day: 20. 02. 24.
"""

def go(currentDay, totalPay):
    global ans

    if totalPay > ans and currentDay <= N:
        ans = totalPay
    if currentDay >= N:
        return


    go(currentDay + T[currentDay], totalPay + P[currentDay])
    go(currentDay + 1, totalPay)

ans = 0
T = []
P = []
N = int(input())
for _ in range(N):
    tmpT, tmpP = map(int, input().split())
    T.append(tmpT)
    P.append(tmpP)

go(0, 0)
print(ans)




"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
>
45
--------------
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
>
55
----------
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
>
20
----------
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
>
90
"""
