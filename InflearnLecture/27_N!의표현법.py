'''
    @ 27. N!의 표현법
    @ Idea. 소수 구하는 방법
    @ TestCase:
        input 1: 5
        output 1: 3 1 1

        input 2: 7
        output 2: 4 2 1 1

    @ Start day: 19. 09. 22
    @ End day: 19. 09. 22
'''

N = int(input("N! 표현법으로 표현할 숫자를 입력해주세요."))

ch = [0] * (N+1) # 0 ~ N-1 까지의 숫자가 들어가야하니깐.

for i in range(2, N+1): # 2 ~ N까지
    tmp = i
    j = 2
    while True:
        if tmp % j == 0:
            tmp = tmp / j
            ch[j] += 1
        else:
            j += 1

        if tmp == 1:
            break

result = str(N) + "! = "
for i in range(len(ch)):
    if ch[i] is not 0:
        result = result + str(ch[i]) + " "

print(result)