"""
    @ Baek 2592 대표값
    @ Prob. https://www.acmicpc.net/problem/2592
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

from collections import Counter

arr = [int(input()) for _ in range(10)]
mode_dic = Counter(arr)
modes = mode_dic.most_common()

print(sum(arr) // 10)
print(modes[0][0])


"""
10
40
30
60
30
20
60
30
40
50
>
37
30
"""