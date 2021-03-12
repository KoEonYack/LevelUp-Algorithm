'''
    @ SWEA-1961 숫자 배열 회전
    @ Prob. https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq
      Ref. None
    @ Algo:
    @ Start day: 19. 09. 09
    @ End day: 19. 09. 09
'''

NumOfTestCase = int(input("Test case"))
itr = 1

while itr <= NumOfTestCase:
    itr += 1
    N = int(input("Arr Size"))
    arr = [[] for i in range(N)]

    # 결과 초기화
    results = ["" for i in range(N)]

    # 배열 입력
    for i in range(N):
        elementsStr = input()
        arr[i] = list(map(int, elementsStr.split()))

    # 모든 가로 elements 에 대해서 회전 변환 시도
    for i in range(N):
        for j in range(N):           # 90도 일 때
            results[i] += str(arr[N-1-j][i]) + " "

        for k in range(N-1, -1, -1): # 180도 일 때
            results[i] += str(arr[N-1-i][k]) + " "

        for l in range(N):           # 270도 일 때
            results[i] += str(arr[l][N-1-i])

    # 결과 출력
    print("#{0}".format(itr))
    for result in results:
        print(result)
