'''
    @ 28. N!에서 0의 갯수
    @ Idea.
    @ TestCase:
        input 1: 5 (5! = 120)
        output 1: 1

        input 1: 12 (12! = 479001600)
        output 2: 2
    @ Start day: 19. 10. 14
    @ End day: 19. 10. 14
'''

# 풀이 1
'''
N = 1
length = 12 # 12!
for i in range(1, length+1):
    N = N * i

strNum = str(N)
cnt = 0
maxLen = 0

preChar = strNum[0]

for i in range(1, len(strNum)):
    currChar = strNum[i]
    if currChar is '0' and preChar is '0':
        cnt += 1
    elif currChar is '0':
        cnt += 1
    else:
        cnt = 0
    if cnt > maxLen:
        maxLen = cnt
    preChar = currChar

print(maxLen)
'''

N = 12
cnt1, cnt2 = 0, 0
for i in range(2, N+1):
    tmp = i
    j = 2
    while True:
        if tmp % j == 0:
            if j == 2:
                cnt1 += 1
            elif j == 5:
                cnt2 += 1
            tmp = tmp/j
        else:
            j += 1
        if tmp == 1:
            break

if cnt1 < cnt2:
    print(cnt1)
else:
    print(cnt2)