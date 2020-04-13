"""
    @ Baek 2738 삼각 김밥
    @ Prob. https://www.acmicpc.net/problem/2738
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 13.
    @ End day: 20. 04. 13.
"""

seven25_Gram, seven25_P = map(int, input().split())
g_per_p = seven25_Gram * 1000 / seven25_P
for _ in range(int(input())):
    G, P = map(int, input().split())
    g_per_p = min(g_per_p, G * 1000 / P)

print("%.2f" % (g_per_p))


"""
5 100
3
4 100
3 100
7 100

"""