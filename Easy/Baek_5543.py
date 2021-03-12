"""
    @ Baek 5543 상근날드
    @ Prob. https://www.acmicpc.net/problem/5543
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""


arr = []
for _ in range(5):
    arr.append(int(input()))

print(min(arr[0], arr[1], arr[2]) + min(arr[3], arr[4]) - 50)


"""
800
700
900
198
330
> 
848
"""