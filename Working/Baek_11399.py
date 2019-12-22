'''
    @ Baek 11399
    @ Prob. https://www.acmicpc.net/problem/11399
      Ref.
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 22.
    @ End day:
'''


def DFS(VertexNum):
    cache = []
    global answer

    if VertexNum is N:
        cumSum = 0
        print(VertexNum, N, Sequence)
        for j in range(N):
            for k in range(0, j):
                print(arr[Sequence[k]], cumSum, k, j)
                cumSum += arr[Sequence[k]]

        if cumSum < answer:
            answer = cumSum
            print(answer)

    for i in range(N):
        if Vertex[i] is False:
            Vertex[i] = True
            Sequence.append(i)
            DFS(VertexNum+1)
            Sequence.remove(Sequence[-1])
            Vertex[i] = False

    return

answer = 987654321
N = int(input())
arr = list(map(int, input().split()))
Sequence = []
Vertex = [False] * N
DFS(0)
print("[" , answer , "]")

'''
5
3 1 4 3 2
[ 3 1 4 3 2 ]
3
3 + 3
2 + 3 + 4 
'''