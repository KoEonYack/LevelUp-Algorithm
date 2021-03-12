"""
    @ Baek 3040 백설 공주와 일곱 난쟁이
    @ Prob. https://www.acmicpc.net/problem/3040
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""


arr = [int(input()) for i in range(9)]
total_sum = sum(arr)
flag = False
for i in range(8):
    if flag is True:
        break
    for j in range(i+1, 9):
        if total_sum - (arr[i] + arr[j]) == 100:
            arr.pop(i)
            arr.pop(j-1)
            #arr = [str(i) for i in arr]
            #print("\n".join(arr))
            print(*sorted(arr), sep="\n")
            flag = True
            break

"""
7
8
10
13
15
19
20
23
25
>
7
8
10
13
19
20
23
"""