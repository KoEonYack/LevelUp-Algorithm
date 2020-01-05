"""
    @ Baek 11729 하노이 탑 이동 순서
    @ Prob. https://www.acmicpc.net/problem/11729
      Ref. https://pacific-ocean.tistory.com/119
      Ref Prob.
    @ Algo: 구현(재귀)
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""


def hanoi(N, start, by, end):
    global step
    if N == 1:
        print(start, end)
    else:
        hanoi(N-1, start, end, by)
        step += 1
        print(start, end)
        hanoi(N-1, by, start, end)

step = 0
N = int(input())
print(pow(2, N) - 1)
hanoi(N, 1, 2, 3)


# 사실 하노이는 2 ^ 원반의 갯수 - 1을 해서 프린트 해주면
"""
우선 하노이탑 이동 규칙에 대해 살펴보자.
n개의 원판이 있을때, n - 1개의 원판 즉, 맨 밑의 원판을 제외하고 나머지 원판들을
1번에서 2번으로 옮긴 뒤, 맨 밑의 원판을 1번에서 3번으로 옮긴다.
그리고 n - 1개의 원판들을 다시 2번에서 3번으로 옮긴다.
이 규칙만 완벽하게 이해한다면 문제를 풀기 수월하다.


3
>

"""