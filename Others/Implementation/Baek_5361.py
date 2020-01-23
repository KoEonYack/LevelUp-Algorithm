"""
    @ Baek 5361 전투 드로이드 가격
    @ Prob. https://www.acmicpc.net/problem/5361
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

val = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(5):
        ans += (arr[i] * val[i])
    print("$%.2f" % ans)

"""
3
20 10 14 3 9
19 17 12 8 10
11 9 8 22 33
>
$13987.50
$15679.76
$16182.54
"""