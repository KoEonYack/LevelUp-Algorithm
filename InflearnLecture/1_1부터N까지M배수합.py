'''
    @ 1. 1부터 N까지 M배수 합
    @ Idea.
    @ TestCase: 15 3
                3 + 6 + 9 + 12 + 15 = 45
    @ Start day: 19. 09. 29
    @ End day: 19. 09. 29
'''


N, multi = map(int, input().split())
num = 0
for i in range(1, N+1): # 1 ~ N
    if i % multi is 0:
        num += i

print(num)

