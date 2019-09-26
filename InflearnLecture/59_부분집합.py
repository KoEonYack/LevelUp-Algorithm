'''
    @ 59. 부분집합
    @ Idea. DFS
    @ TestCase: 3
    @ output:
        1 2 3
        1 2
        1 3
        1
        2 3
        2
        3
        (empty)
    @ Start day: 19. 09. 26
    @ End day: 19. 09. 26
'''

def DFS(L):
    if L is n+1: # 마지막 레벨에 도달했을 때
        for i in range(1, n+1): # 1 ~ n
            if ch[i] is 1:
                print(i, end=' ')
        print()
    else:
        ch[L] = 1 # 좌측 브렌치를 탈 때 1로
        DFS(L+1)
        ch[L] = 0 # 우측 브렌치를 탈 때 0으로
        DFS(L+1)

ch = [0] * 11
n = int(input())
DFS(1)