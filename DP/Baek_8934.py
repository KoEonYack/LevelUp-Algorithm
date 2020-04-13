"""
    @ Baek 8394. 약수
    @ Prob. https://www.acmicpc.net/problem/7384
     Ref.
    @ Algo: DP
    @ Start day: 20. 04. 12.
    @ End day: 20. 04. 12.
"""


fibo = [0] * 10000001
N = int(input())

fibo[0] = 1
fibo[1] = 1
fibo[2] = 2

for i in range(3, len(fibo)):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 10

print(fibo[N])

