'''
    @ 술레잡기
    @ Prob. https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/?fbclid=IwAR1ZJ7Fc5OqNY6UM8bvPfyCndMxJUNRyeRVB6aapWazjJwFl5uu4JNcubig
      Ref.
    @ Algo: BFS
    @ Start day: 19. 09. 20
    @ End day:
'''


def sol(ConyInitPos, BrInitPos):
    q = []
    q.append((BrInitPos, 0))
    time = 0
    ConyPos = ConyInitPos

    while True:

        if ConyPos > 2000:
            return -1

        if(visit[ConyPos]):

#ConyInitPos, BrInitPos = map(int, input().split())
visit = [[False, -1] for _ in range(2001)]
print(sol(BrInitPos))

