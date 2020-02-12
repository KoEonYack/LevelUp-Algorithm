"""
    @ Baek 2110 공유기 설치
    @ Prob. https://www.acmicpc.net/problem/2110
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 20. 02. 12.
    @ End day: 20. 02. 12.
"""


def check(x):
    last = arr[0]
    cnt = 1                 # 수정2
    for i in range(1, len(arr)):
        if arr[i] - last >= x:
            cnt += 1
            last = arr[i]

    return cnt


N, C = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()
start = 1
end = arr[-1] - arr[0] # 수정1
ans = 0
while start <= end:
    mid = (start + end) // 2
    possible_num = check(mid)
    #print(mid, possible_num)

    if possible_num >= C: # 길이를 키워리 
        start = mid + 1
        if mid > ans: # possible num으로 함 [여기가 핵심]
            ans = mid
    else:                 # 길이를 줄여라
        end = mid - 1


print(ans)

"""
5 3
1
2
8
4
9
>
3
"""