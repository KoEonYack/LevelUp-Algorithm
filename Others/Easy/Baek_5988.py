"""
    @ Baek 5988 홀수일까 짝수일까
    @ Prob. https://www.acmicpc.net/problem/5988
      Ref.
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

N = int(input())
for _ in range(N):
    num = int(input())
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


"""
2
1024
5931
>
even
odd
"""