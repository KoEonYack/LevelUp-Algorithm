"""
    @ Baek 1062. 가르침
    @ Prob. https://www.acmicpc.net/problem/1062
     Ref.
    @ Algo: BFS
    @ Start day: 20. 09. 28.
    @ End day: 20. 09. 28.
"""

import sys


def DFS(idx, cnt):
    global ans

    if cnt == K-5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not check[ord(w) - ord('a')]:
                    break
            else:
                read_cnt += 1
        ans = max(ans, read_cnt)
        return

    for i in range(idx, 26):
        if not check[i]:
            check[i] = True
            DFS(i, cnt + 1)
            check[i] = False

            
N, K = map(int, input().split())
check = [False] * 26
ans = 0
# 종료 K
if K < 5:
    print(0)
    sys.exit(0)
elif K == 26:
    print(N)
    sys.exit(0)

words = [set(map(str, input())) for _ in range(N)]

# 배워야만 하는 단어
for c in ['a', 'c', 'i', 'n', 't']:
    check[ord(c) - ord('a')] = True

DFS(0, 0)
print(ans)

    
    
    

"""
3 6
antarctica
antahellotica
antacartica
>
2

for와 함께 쓰는 else는, for문이 중간에 break 등으로 끊기지 않고,
끝까지 수행 되었을 때 수행하는 코드를 담고 있습니다.
"""
