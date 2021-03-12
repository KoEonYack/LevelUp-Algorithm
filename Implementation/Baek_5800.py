"""
    @ Baek 5800 성적 통계
    @ Prob. https://www.acmicpc.net/problem/5800
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for i in range(int(input())):
    N, *arr = map(int, input().split())
    arr.sort(reverse=True)
    diff = 0
    for j in range(1, len(arr)):
        if arr[j-1] - arr[j] > diff:
            diff = arr[j-1] - arr[j]

    print("Class", i+1)
    print("Max " + str(max(arr)) + ", Min " + str(min(arr)) + ", Largest gap", diff)



"""
2
5 30 25 76 23 78
6 25 50 70 99 70 90
>
Class 1
Max 78, Min 23, Largest gap 46
Class 2
Max 99, Min 25, Largest gap 25
"""