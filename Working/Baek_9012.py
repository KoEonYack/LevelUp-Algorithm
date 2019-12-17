'''
    @ Baek 9012
    @ Prob. https://www.acmicpc.net/problem/9012
      Ref.
            정답: https://hwiyong.tistory.com/187
            숫자로 풀기 : https://pacific-ocean.tistory.com/70
            짝 맞춰서 풀기 : https://ksw626.tistory.com/96
      Ref Prob. https://parkssiss.tistory.com/35
    @ Algo: Stack
    @ Start day: 19. 12. 15
    @ End day:
'''


def solution(inputStr):
    stack = []

    for char in inputStr:
        if char is "(":
            stack.append(char)
        elif char is ")":
            #print(stack[:-1])
            if len(stack) is not 0 and stack[-1] is '(':
                stack.pop()
            else:
                print("No")
                return

    if len(stack) is 0:
        print("Yes")
    else:
        print("No")

    return


N = int(input())
for _ in range(N):
    inputStr = input()
    solution(inputStr)

'''
for i in range(N):
    solution(strArr[i])
'''

