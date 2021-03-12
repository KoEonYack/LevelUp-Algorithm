"""
    @ Baek 1145 적어도 대부분의 배수
    @ Prob. https://www.acmicpc.net/problem/1145
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 24.
    @ End day: 20. 05. 24.
"""

arr = list(map(int, input().split()))
i = min(arr)
while 1:
    cnt = 0
    for j in range(len(arr)):
        if i % arr[j] == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break
    else:
        i += 1


"""
30 42 70 35 90
>
210
"""
