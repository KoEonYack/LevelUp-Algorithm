'''
    @ 14. 뒤집은 소수
    @ Idea. 자릿수
    @ TestCase:
        input   5
                32 55 62 3700 250

        output 23 73
    @ Start day: 19. 10. 07
    @ End day: 19. 10. 07
'''


def isPrime(x):
    if x == 1:
        return False
    else:
        for a in range(2, x):
            if x % a == 0:
                return False
    return True

def Reverse(x):
    return int(str(x)[::-1])

# NumArr = map(int, input("숫자를 입력해주세요").split())
NumArr = [32, 55, 62, 3700, 250]

for num in NumArr:
    num = Reverse(num)
    if(isPrime(num)):
        print(num, end=" ")

