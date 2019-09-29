'''
    @ 3. 진약수의 합
    @ Idea.
    @ TestCase: 20
                1 + 2 + 4 + 5 + 10 = 22
    @ Start day: 19. 09. 29
    @ End day: 19. 09. 29
'''


N = int(input())
num = 0
print("1 ", end="")
num += 1
for i in range(2, N): # 1 ~ N
    if N % i is 0:
        print("+ ", end="")
        num += i
        print(i, end=' ')
print("= " + str(num))
