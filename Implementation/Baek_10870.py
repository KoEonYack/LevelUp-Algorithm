"""
    @ Baek 10870 피보나치 수 5
    @ Prob. https://www.acmicpc.net/problem/10870
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 22
    @ End day: 20. 01. 22
"""

def fibo(Num):
    if Num == 0:
        return 0
    elif Num == 1:
        return 1
    else:
        return fibo(Num-1) + fibo(Num-2)


N = int(input())
print(fibo(N))

"""
10
>
55
"""