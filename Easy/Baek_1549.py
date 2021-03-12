"""
    @ Baek 1549 평균
    @ Prob. https://www.acmicpc.net/problem/1549
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""


N = int(input())
arr = list(map(int, input().split()))
maxV = max(arr)
new_total_score = 0
for i in range(N):
    new_total_score += (arr[i] / maxV) * 100

print(new_total_score/N)

"""
점수/M*100 -> 평균

3
10 20 30
>
66.666667

4
1 100 100 100
>
75.25
"""
