"""
    @ Baek 1449
    @ Prob. https://www.acmicpc.net/problem/1449
      Ref. https://donggod.tistory.com/89
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 25
    @ End day: 19. 12.
"""



N, TapSize = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
min = arr[0]
answer = 1

for i in range(1, N):
    if arr[i] - min > TapSize - 1:
        min = arr[i]
        answer += 1

print(answer)

"""
4 2
1 2 100 101
> 2
"""
