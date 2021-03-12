"""
    @ 백준 10990 별 찍기 - 15
    @ https://www.acmicpc.net/problem/10990
    @ End Day : 2020. 01. 29.
"""

N = int(input())

for i in range(N):
    print(" " * (N - (i+1)) + "*" + " " * (2 * (i) - 1), end="")
    if i is not 0:
        print("*", end="")
    print()


"""
4
>
   *
  * *
 *   *
*     *
"""