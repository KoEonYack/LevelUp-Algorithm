'''
    @ [Level 1] K번째 수
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42748
      Ref. None
    @ Algo: Sorting
    @ Start day: 19. 09. 06
    @ End day: 19. 09.
'''

'''
예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
1.array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2.1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3.2에서 나온 배열의 3번째 숫자는 5입니다.
'''

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        partArr = array[commands[i][0]-1:commands[i][1]]
        partArr = sorted(partArr)                # 부분 배열 정렬
        answer.append(partArr[commands[i][2]-1]) # n번째 숫자
    return answer

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

'''
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
'''