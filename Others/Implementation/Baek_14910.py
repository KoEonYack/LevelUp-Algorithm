"""
    @ Baek 14910 오르막
    @ Prob. https://www.acmicpc.net/problem/14910
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

arr = list(map(int, input().split()))
flag = False
for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
        flag = True
        break

if flag is True:
    print("Bad")
else:
    print("Good")


"""
1 2 3 4 5
>
Good
-------------

"""