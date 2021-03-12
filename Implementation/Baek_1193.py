"""
    @ Baek 1193 분수찾기
    @ Prob. https://www.acmicpc.net/problem/1193
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 15
    @ End day: 20. 01. 15
"""


N = int(input())

cnt = 0
while N > 0:
    cnt += 1
    N -= cnt

if cnt % 2 == 0:
    print(str(cnt+N) + "/" + str(1 + (-N)))
else:
    print(str(1+(-N)) + "/" + str(cnt + N))


"""
14
>
2/4
"""
