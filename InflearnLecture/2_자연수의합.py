'''
    @ 2. 자연수의 합
    @ Idea.
    @ TestCase: 3 7
                3 + 4 + 5 + 6 + 7 = 25
    @ Start day: 19. 09. 29
    @ End day: 19. 09. 29
'''

start, end = map(int, input().split())
num = 0
for i in range(start, end+1):
    num += i
print(num)