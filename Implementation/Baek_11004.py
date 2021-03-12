"""
    @ Baek 11004 K번째 수
    @ Prob. https://www.acmicpc.net/problem/11004
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[K - 1])


"""
5 2
4 1 2 3 5
>
2
"""