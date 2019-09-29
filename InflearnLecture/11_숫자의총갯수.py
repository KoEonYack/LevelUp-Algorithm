'''
    @ 11. 숫자의 총 갯수
    @ Idea. 수의 나눗셈 -> 파이썬은 소숫점으로 내려가기 때문에 이렇게 풀면 안됨
    @ TestCase: 3
                125 15232 97
    @ Start day: 19. 09. 29
    @ End day: 19. 09. 29
'''


N = int(input("Enter N>"))
ans = 0
tmp = 0
for i in range(1, N+1): # 1 ~ N
    tmp = i

    while tmp > 0.11:
        tmp = tmp / 10
        ans += 1

print(ans)