"""
    @ Baek 11652 카드
    @ Prob. https://www.acmicpc.net/problem/11652
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 20. 02. 12.
    @ End day: 20. 02. 12.
"""

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

ans = arr[0]
ans_cnt = 1
cnt = 1
for i in range(1, N):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt = 1

    if ans_cnt < cnt:
        ans_cnt = cnt
        ans = arr[i]

print(ans)

"""
5
1
2
1
2
1
>
1
-----------------------
7
1
2
1
2
1
2
3
>
1
"""