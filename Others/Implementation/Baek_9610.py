"""
    @ Baek 9610 사분면
    @ Prob. https://www.acmicpc.net/problem/9610
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

Q1 = Q2 = Q3 = Q4 = AXIS = 0


for i in range(int(input())):
    X, Y = map(int, input().split())
    if X == 0 or Y == 0:
        AXIS += 1
    elif X > 0 and Y > 0:
        Q1 += 1
    elif X < 0 and Y > 0:
        Q2 += 1
    elif X < 0 and Y < 0:
        Q3 += 1
    elif X > 0 and Y < 0:
        Q4 += 1

print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", AXIS)


"""
5
0 0
0 1
1 1
3 -3
2 2
>
Q1: 2
Q2: 0
Q3: 0
Q4: 1
AXIS: 2
"""