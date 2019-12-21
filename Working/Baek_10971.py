'''
    @ Baek 10971
    @ Prob. https://www.acmicpc.net/problem/10971
      Ref.
            https://hibee.tistory.com/225
      Ref Prob.
    @ Algo: Backtracking
    @ Start day: 19. 12. 21
    @ End day:
    @ Memo:
        - 종이에 구현 방법 작성함.
        - X! 의 시간복잡도.
        - PyPy3로 제출해야 시간 초과가 안나옴(Python 3로 제출시 시간초과)
'''


def DFS(NodeNum):

    if NodeNum is N:
        res = 0
        for i in range(len(path)-1):
            currPath = path[i]
            nextPath = path[i+1]

            #print("[" + str(path) + "]")
            #for a in InputArr:
            #    print(a)
            #print(currPath, nextPath)
            if InputArr[currPath][nextPath] is 0:
                return
            else:
                res += InputArr[currPath][nextPath]

        if InputArr[path[len(path)-1]][path[0]] != 0:
            global ans
            res += InputArr[path[len(path) - 1]][path[0]]
            ans = min(res, ans)
        return

    for i in range(1, N+1): # 1 ~ N
        if visited[i] is False:
            path.append(i)
            visited[i] = True
            DFS(NodeNum+1)
            visited[i] = False
            path.remove(path[-1])

    return



path = []
ans = 987654321

N = int(input())

InputArr = []
visited = [False] * (N+1)

InputArr.append([0] * (N + 1))
for _ in range(N):
    InputArr.append([0] + list(map(int, input().split())))


#print("------------------")
#for c in InputArr:
#    print(c)
#print("------------------")

DFS(0)
print(ans)
