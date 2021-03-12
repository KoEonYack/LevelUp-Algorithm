"""
    @ Baek 1181
    @ Prob. https://www.acmicpc.net/problem/1181
      Ref.
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 01. 04
    @ End day:  20. 01. 04
"""


N = int(input())
arr = []
for _ in range(N):
    inputStr = input()
    arr.append((inputStr, len(inputStr)))

# 중복 제거
arr = list(set(arr))

# 숫자, 배열
arr.sort(key=lambda x: (x[1], x[0]))

for word in arr:
    print(word[0])

"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

> 
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""