"""
    @ Baek 11652 카드
    @ Prob. https://www.acmicpc.net/problem/11652
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""

from collections import Counter
import sys

arr = []
for i in range(int(input())):
    arr.append(int(sys.stdin.readline()))

mode_dict = Counter(arr)
modes = mode_dict.most_common()

modes.sort(key=lambda x:x[1], reverse=True)

max_common = modes[0][1]
prev = modes[0][0]
for a, b in modes:
    if max_common > b:
        print(prev)
        break
    prev = a


"""
5
3
3
1
1
2
>
1
--------------
6
1
2
1
2
1
2
>
1


6
1
2
3
4
5
6

"""