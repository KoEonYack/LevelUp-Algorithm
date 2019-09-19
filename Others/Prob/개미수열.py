'''
    @ 개미수열
    @ Prob. https://heecheolman.tistory.com/3
      Ref. https://heecheolman.tistory.com/3
    @ Start day: 19. 09. 19
    @ End day:
'''


def AntSeq(N):
    currAr = [1]
    nextAr = []

    for i in range(len(currAr)):
        nextAr.append(currAr[i])


N = int(input())
AntSeq(N)