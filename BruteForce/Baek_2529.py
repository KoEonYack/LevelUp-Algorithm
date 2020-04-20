"""
    @ Baek 2529. 부등호
    @ Prob. https://www.acmicpc.net/problem/2529
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 04. 20.
    @ End day: 20. 04. 20.
"""

K = int(input())
arr = list(map(str, input().split()))

small = [0] * (K+1)
big = [0] * (K+1)

for i in range(K+1):
    small[i] = i
    big[i] = 9-i

"""
do: 
    task() 
while condition



while True
    task()
    if condition continue
    break

"""

while True:
    if check(small, a):
        break
    if next_permutation(): continue

    break




"""
2
< > 
>
897
021
"""