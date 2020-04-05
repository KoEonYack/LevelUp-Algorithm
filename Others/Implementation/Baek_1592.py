"""
    @ Baek 1592 영식이와 친구들
    @ Prob. https://www.acmicpc.net/problem/1592
      Ref.
      Ref Prob.
    @ Algo: 시뮬레이션
    @ Start day: 20. 04. 03.
    @ End day: 20. 04. 03.
"""

# 공을 M번 보다 적게 받은 사람이 공을 던질 때, 현재 공을 받은 횟수가 홀수번이면
# 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게,
# 짝수번이면 자기의 현재 위치에서 반시계 방향으로 L번째 있는 사람에게 공을 던진다.
# 종료 조건, 한 사람이라도 M 번 받으면 종료

N, M, L = map(int, input().split())
countBall = [0] * N
countBall[0] = 1
res = 0
idx = 0
while max(countBall) != M:
    if countBall[idx] % 2: # 던진 횟수 짝수 -> 반시계방향
        countBall[(idx - L) % N] += 1
        idx = (idx - L) % N

    else: # 던진 횟수 홀수 -> 시계방향
        countBall[(idx + L) % N] += 1
        idx = (idx + L) % N

    res += 1

print(res)

"""
5 3 2
>
10
"""