'''
    @ 29. 3의 개수는(small)
    @ Idea.
    @ TestCase:
        input: 15
        output: 2

        input: 12345
        output: 4721
    @ Start day: 19. 10. 09
    @ End day: 19. 10. 09
'''

N = int(input())
result = 0

for num in range(1, N+1): # 1~N
    while num > 0:
        if num % 10 == 3:
            result += 1
        num = num / 10

print(result)
