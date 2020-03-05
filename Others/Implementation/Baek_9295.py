"""
    @ Baek 9295 주사위
    @ Prob. https://www.acmicpc.net/problem/9295
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for i in range(1, int(input())+1):
    print("Case " + str(i) + ":", sum(list(map(int, input().split()))))


"""
5
1 2
1 3
3 5
2 6
3 4
>
Case 1: 3
Case 2: 4
Case 3: 8
Case 4: 8
Case 5: 7
"""