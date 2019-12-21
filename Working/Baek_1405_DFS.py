'''
    @ Baek 1405 (Solve)
    @ Prob. https://www.acmicpc.net/problem/1405
      Ref.
            https://kswims.tistory.com/173
            https://www.crocus.co.kr/678
      Ref Prob.
    @ Algo: Backtracking(DFS)
    @ Start day: 19. 12. 18
    @ End day: 19. 12. 19
'''

def solution(Pair, curr, result):
    global total

    if curr == N+1:
        total += result
        return;

    visited[Pair[0]][Pair[1]] = 1

    for i in range(4):
        nextx = Pair[0] + dx[i]
        nexty = Pair[1] + dy[i]

        if visited[nextx][nexty] == 0:
            solution([nextx, nexty], curr+1, result*percent[i])

    visited[Pair[0]][Pair[1]] = 0
    return;


N, e, w, s, n = list(map(int, input().split()))
percent = [e/100, w/100, s/100, n/100]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0] * 29 for _ in range(29)]
total = 0
solution([14, 14], 1, 1.0)
print(total)

