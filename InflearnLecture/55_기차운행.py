'''
    @ 55. 기차 운행
    @ Idea. 스택,
            종료 조건: 모든 자동차가 들어왔을 때 스택이 비어있지 않는다면 Impossible
    @ TestCase:
        input:  3
                2 1 3
        output: PPOOPO
    @ Start day: 19. 10. 09
    @ End day: 19. 10. 09
'''

N = 3
inputArr = [2, 1, 3]
ExpectArr = [i for i in range(1, N+1)] # 1 ~ N
stack = []


while len(ExpectArr) != 0: # 예상 값이 다 사라지면 반복문 종료
    if len(inputArr) == 0 and len(stack) > 0 and len(stack) > 0: # 더 이상 들어올 값이 없을 경우
        print("Impossible")
        break

    if len(inputArr) != 0:
        num = inputArr.pop()
        stack.append(num)
        print("P", end=" ")

    print(stack)
    print(ExpectArr)
    if stack[-1] == ExpectArr[0]:
        ExpectArr.pop()
        stack.remove(stack[-1])
        print("O", end=" ")
        continue
    else:
        continue

