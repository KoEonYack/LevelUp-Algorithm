'''
    @ 45. 공주 구하기
    @ Idea. 조세푸스
    @ TestCase:
        input:  8 3
        output: 7
    @ Start day: 19. 10. 14
    @ End day: 19. 10. 14
'''

N, K = 8, 3
Prince = [0] * (N+1) # 1 ~ 8 까지 배열 생성
pos = 0
bp = 0
cnt = 0
while True:
    pos += 1
    if pos > N:
        pos = 1
    if Prince[pos] == 0:
        cnt += 1
        if cnt == K:
            Prince[pos] = 1
            cnt = 0
            bp += 1
    if bp == N-1:
        break
