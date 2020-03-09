"""
    @ Baek 2566 최댓값
    @ Prob. https://www.acmicpc.net/problem/2566
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

arr = list(list(map(int, input().split())) for _ in range(9))

max_i = max_j = 0
max_v = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_v:
            max_v = arr[i][j]
            max_i = i+1
            max_j = j+1

print(max_v)
print(max_i, max_j)


"""
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80
>
90
5 7
"""
