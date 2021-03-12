"""
    @ 1912. 연속합
    @ Prob. https://www.acmicpc.net/problem/1912
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 30.
    @ End day: 20. 01. 30.
"""

N = int(input())
arr = list(map(int, input().split()))

maxSumEndingHere = 0
maxSumSoFar = 0

for num in arr:
    maxSumEndingHere += num
    if maxSumEndingHere < 0:
        maxSumEndingHere = 0

    if maxSumEndingHere > maxSumSoFar:
        maxSumSoFar = maxSumEndingHere

flag = False
for num in arr:
    if num > 0:
        flag = True

if flag is False:
    print(max(arr))
else:
    print(maxSumSoFar)

"""
10
10 -4 3 1 5 6 -35 12 21 -1
>
33
"""