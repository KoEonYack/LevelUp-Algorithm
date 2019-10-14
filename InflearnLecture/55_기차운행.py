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
arriveArr = [i for i in range(1, N+1)] # 1 ~ N
stack = []
step = []
while len(inputArr) > 0:



if len(arriveArr) == 0:
    print(step)
else:
    print("Impossible")