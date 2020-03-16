"""
    @ Baek 2729 이진수 덧셈
    @ Prob. https://www.acmicpc.net/problem/2729
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

for _ in range(int(input())):
    A, B = map(str, input().split())
    tenA = int(A, 2)
    tenB = int(B, 2)
    print(bin(tenA+tenB)[2:])


"""
3
1001101 10010
1001001 11001
1000111 1010110
>
1011111
1100010
10011101
"""