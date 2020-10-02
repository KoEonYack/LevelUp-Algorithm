"""
    @ Baek 1700. 멀티탭 스케줄링
    @ Prob. https://www.acmicpc.net/problem/1700
      Ref. https://jaimemin.tistory.com/759
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 24
    @ End day: 20. 09. 29.
"""


# N, K : 멀티탭 구멍의 갯수, K 전기 용품의 총 사용 횟수
N, K = map(int, input().split())

plans = list(map(int, input().split()))
use = [0] * N

for plan in plans:
    # 전기 용품이 이미 꽃혀 있는지
    if plan in use:
        continue

    # 비어 있는 구멍이 있는지 확인
    if 0 in use:
        use[use.index(0)] = plan
        continue

    # 가장 나중에 사용
    # 앞으로 사용하지 않을 것
    for j in N:
        pass



"""
2 7
2 3 2 3 1 2 7
> 2
"""