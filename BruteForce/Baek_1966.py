"""
    @ 1966. 크게 만들기
    @ Prob. https://www.acmicpc.net/problem/2812
     Ref.
    @ Algo: B
    @ Start day: 20. 02. 02.
    @ End day: 20. 02. 02.
"""

testcase=int(input())
answer=[]
for test in range(testcase):
    que = []
    N,M=map(int,input().split(" ")) # N=문서의수 M=원하는 문서 인덱스
    qurio = list(map(int,input().split(" "))) # 중요도순서
    qurio = [(data,index) for index, data in enumerate(qurio)] # [[1,0],[0,1]].. 순으로 인덱스 매겨져서 우선순위가 적용됨.
    count = 0
    while(True):
        if qurio[0][0] == max(qurio, key=lambda x: x[0])[0]: #가장 큰 우선순위라면
            count += 1
            if qurio[0][1] == M: # 내가 원하는 문서라면
                answer.append(count)
                break
            else: # 원하는 문서가 아니라면
                qurio.pop(0) #가장 큰 우선순위니까 뽑는다. else:
            temp=qurio.pop(0)
            qurio.append(temp)
for prt in answer:
    print(prt)


"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
>
1
2
5

"""