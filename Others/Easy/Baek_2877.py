"""
    @ Baek 2877 ??
    @ Prob. https://www.acmicpc.net/problem/2877
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

N = int(input())
biNum = str(bin(N-1))
print(biNum)
biNum = biNum.replace("0", "4").replace("1", "7")
print(biNum[2::])

"""
4 -> 0
7 -> 1

1
>
4

2
>
7

3
>
44
"""