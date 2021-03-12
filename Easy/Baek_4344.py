"""
    @ Baek 4344 평균은 넘겠지
    @ Prob. https://www.acmicpc.net/problem/4344
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""


N = int(input())
for _ in range(N):
    over_avg_stu = 0
    arr = list(map(int, input().split()))
    avg = sum(arr[1:arr[0]+1]) / arr[0]
    for i in range(1, arr[0]+1):
        if arr[i] > avg:
            over_avg_stu += 1
    print("%0.3f" % round(over_avg_stu*100 / arr[0], 3) + "%")

"""
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

>

40.000%
57.143%
33.333%
66.667%
55.556%
"""