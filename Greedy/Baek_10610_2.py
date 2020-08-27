"""
    @ Baek 10610. 30
    @ Prob. https://www.acmicpc.net/problem/10610
     Ref.   
    @ Algo: Greedy
    @ Start day: 20. 08. 26.
    @ End day: 20. 08. 26.
"""



N = [int(i) for i in input()]
N.sort(reverse=True)
if N[-1] == 0 and sum(N) % 3 == 0:
    print("".join(map(str, N)))
else:
    print(-1)


"""
102
>
210
"""

