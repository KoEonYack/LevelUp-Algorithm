"""
    @ Baek 3058 짝수를 찾아라
    @ Prob. https://www.acmicpc.net/problem/3058
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    ans = []
    for num in arr:
        if num % 2 == 0:
           ans.append(num)
    print(sum(ans), min(ans))


"""
2
1 2 3 4 5 6 7
13 78 39 42 54 93 86
>
12 2
260 42
"""