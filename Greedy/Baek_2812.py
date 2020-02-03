"""
    @ 2812. 크게 만들기
    @ Prob. https://www.acmicpc.net/problem/2812
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 02.
    @ End day: 20. 02. 02.
"""

N, K = input().split()
input_str = input()
num_arr = list(input_str)
num_arr.sort(reverse=True)
for _ in range(int(K)):
    num_arr.pop()

if len(num_arr) is 0:
    print(0)
else:
    print("".join(num_arr))




"""'
4 2
1924
>
94

4 4
1111

"""

