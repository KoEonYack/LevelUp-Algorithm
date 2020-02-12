"""
    @ Baek 1654  랜선 자르기
    @ Prob. https://www.acmicpc.net/problem/1654
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 20. 02. 12.
    @ End day: 20. 02. 12.
"""

# 기존 막대 K 갯수,
K, N = map(int, input().split())
arr_K = []
for _ in range(K):
    arr_K.append(int(input()))

start = 1
end = max(arr_K)
mid = 0
ans = 0
while start <= end:
    mid = (start + end) // 2
    cal = 0
    for num in arr_K:
        cal += num // mid
    #print(mid)

    if cal >= N:             # 너무 많은 갯수로 쪼갰다. -> 막대를 늘려야한다.
        #print(cal, mid)
        if ans < mid:
            ans = mid
        start = mid + 1
    else:           # 너무 적은 갯수로 쪼갰다. -> 막대를 줄여야한다.
        end = mid - 1

print(ans)


"""
4 11
802
743
457
539
>
200
"""