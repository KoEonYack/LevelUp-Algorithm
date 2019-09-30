'''
    @ 4. 나이 차이
    @ Idea.
    @ TestCase: 10
                13 15 34 23 45 65 33 11 26 42
    @ Start day: 19. 09. 30
    @ End day: 19. 09. 30
'''


N = int(input())
Arr = list(map(int, input().split()))
max = 0
min = 0

max = Arr[0]
min = Arr[0]
for i in range(len(Arr)):
    if max < Arr[i]:
        max = Arr[i]
    elif min > Arr[i]:
        min = Arr[i]

print(max - min)