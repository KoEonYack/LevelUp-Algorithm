'''
    @ 10. 자릿수의 합
    @ Idea.
    @ TestCase: 3
                125 15232 97
    @ Start day: 19. 09. 29
    @ End day: 19. 09. 29
'''

N = int(input("Input N>"))
Arr = list(map(str, input().split()))
max = 0
num = 0
answer = ""
print(Arr)
for str in Arr:

    for a in str:
        num += int(a)

    if num > max:
        max = num
        answer = str
    num = 0

print(answer)