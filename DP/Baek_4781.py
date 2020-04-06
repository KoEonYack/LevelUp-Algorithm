"""
    @ Baek 4781. 사탕 가게
    @ Prob. https://www.acmicpc.net/problem/4781
     Ref.
    @ Algo: DP(0-1 Knapsack)
    @ Start day: 20. 04. 06.
    @ End day: 20. 04. 06.
"""

DP = [0] * 8 # 100

while True:
    c, p = map(float, input().split())
    if int(c) == 0 and int(p) == 0:
        break



"""
2 8.00
700 7.00
199 2.00
3 8.00
700 7.00
299 3.00
499 5.00
0 0.00
>
796
798

"""
