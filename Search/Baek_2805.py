"""
    @ Baek 2805 나무 자르기
    @ Prob. https://www.acmicpc.net/problem/2805
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 20. 02. 12.
    @ End day: 20. 02. 12.
"""

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)
ans = 0

while start <= end:
    cut_tree = (start + end) // 2
    result = 0
    for num in arr:
        if num - cut_tree > 0:
            result += (num - cut_tree)

    if result >= M:
        if ans < cut_tree:
            ans = cut_tree
        start = cut_tree + 1
    else:
        end = cut_tree - 1

print(ans)


"""
4 7
20 15 10 17
>
15
"""