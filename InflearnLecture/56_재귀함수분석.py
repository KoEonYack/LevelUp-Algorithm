'''
    @ 56. 재귀함수 분석
    @ Idea. 재귀 방식으로 함수를 호출하면 메모리의 스택 영역에 저장된다.
    |   rec(0) - 15번 리턴            |
    |   rec(1) - 라인 17번 까지 실행  |
    |   rec(2) - 라인 17번 까지 실행  |
    |   rec(3) - 라인 17번 까지 실행 |
    @ TestCase:
    @ Start day: 19. 09. 22
    @ End day: 19. 09. 22
'''

def rec(N):
    if N is 0:
        return
    else:
        rec(N = N-1)
        print(N)

N = int(input("시작 숫자를 입력해 주세요."))
rec(N)