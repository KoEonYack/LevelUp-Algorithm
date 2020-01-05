"""
    @ Baek 1157
    @ Prob. https://www.acmicpc.net/problem/1157
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

from collections import Counter

inputStr = input()
inputArr = list(inputStr.upper())
common_dict = Counter(inputArr)
common_arr = common_dict.most_common()
if len(common_arr) > 1: # 1개의 단어로 구성된 경우도 있다.
    if common_arr[0][1] == common_arr[1][1]:
        print("?")
    else:
        print(common_arr[0][0])
else:
    print(common_arr[0][0])

"""
Mississipi
>
?

baaa
> A

aaaaa
> A
"""