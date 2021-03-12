"""
    @ Baek 2747 피보나치 수
    @ Prob. https://www.acmicpc.net/problem/2747
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 23
    @ End day: 20. 01. 23
"""

def fibo(Num):
    if Arr[Num] > 0:
        return Arr[Num]

    if Num == 0:
        return 0
    elif Num == 1:
        return 1
    else:
        Arr[Num] = fibo(Num-1) + fibo(Num-2)
        return Arr[Num]

N = int(input())
Arr = [0] * (N+1)
Arr[1] = 1
print(fibo(N))

"""
10
>
55
"""