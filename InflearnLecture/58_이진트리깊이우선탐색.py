'''
    @ 58. 이진트리 깊이우선탐색
    @ Idea. DFS
    @ TestCase: None
    @ output: 전위, 중위, 후위탐색
    @ Start day: 19. 09. 26
    @ End day: 19. 09. 26
'''


def D(v):
    if v > 7:
        return
    else:
        print(v) # 전위
        D(2*v)
        #print(v) # 중위
        D(2*v+1)
        #print(v) # 후위

D(1)