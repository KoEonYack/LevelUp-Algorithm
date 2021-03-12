"""
    @ Baek 11501. 주식
    @ Prob. https://www.acmicpc.net/problem/11501
      Ref.
    @ Algo: String
    @ Start day: 20. 10. 31
    @ End day:  20. 10. 31
"""

for _ in range(int(input())):
    N = int(input())
    stock = list(map(int, input().split()))
    gain = 0
    max = 0

    for i in range(N-1, -1, -1):
        if stock[i] > max:
            max = stock[i]
        else:
            gain += (max - stock[i])

    print(gain)

"""
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
>>>>
0
10
5
"""