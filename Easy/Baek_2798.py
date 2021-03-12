"""
    백준 2798 블랙잭
    End Day : 2019. 12. 28
"""

from itertools import combinations

N, TargetSum = map(int, input().split())
arr = list(map(int, input().split()))
# combArr = list(combinations(arr, 3))
bigestNum = 0

for ele in list(combinations(arr, 3)):
    currSum = sum(ele)
    if bigestNum <= currSum <= TargetSum:
        bigestNum = currSum

print(bigestNum)

"""

5 21
5 6 7 8 9
> 21

"""