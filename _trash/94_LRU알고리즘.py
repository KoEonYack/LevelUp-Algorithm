'''
    94. LRU 알고리즘
    @ Idea. LRU 알고리즘 설계, 배열
    @ TestCase:

    @ Start day: 19. 12. 02.
    @ End day: 19. 12. 02.
'''

def sol(frame, pages):
    temp = []
    runTime = 0

    if frame == 0:
        runTime = len(pages) * 10
        return runTime
    # cacheSize가 0일때, cities의 크기만큼 10을 곱해주고 끝낸다

    for data in pages:
        if data in temp:                # HIT
            temp.append(temp.pop(0))    # 최신 데이터를 배열의 맨 뒤로
            runTime += 1
        else:                           # MISS
            if len(temp) < frame:       # temp에 공간이 남은 경우
                temp.append(data)
            else:                       # temp에 공간이 남지 않는 경우
                temp = temp[1:] + [data]
                # 가장 사용되지 않은 첫번째 배열을 제거하고 맨 뒤에 입력값을 저장해준다
            runTime += 10
    return runTime

print(sol(3, "BCBAEBCE"))