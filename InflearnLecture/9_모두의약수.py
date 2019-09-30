'''
    @ 9. 모두의 약수
    @ Idea. 문자열 다루기
    @ TestCase: 8
                1 2 2 3 2 4 2 4
    @ Start day: 19. 09. 30
    @ End day: 19. 09. 30
'''

N = int(input())
cnt = [0] * 50001
for i in range(1, N+1): # 1 ~ N
    for j in range(i, N+1,i):
        cnt[j] += 1

for i in range(1, N+1):
    print(cnt[i], end=" ")