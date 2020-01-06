"""
    @ 1655. 가운데를 말해요
    @ Prob. https://www.acmicpc.net/problem/1655
     Ref. https://www.crocus.co.kr/625
    @ Algo: Heap
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

"""
중간 값 구하기 알고리즘
1. 최대 힙의 크기는 최소 힙의 크기와 같거나, 하나 더 크다.
2. 최대 힙의 최대 원소는 최소 합의 최소 원소보다 작거나 같다.
이때 알고리즘에 맞지 않다면 최대 힙, 최소 힙의 가장 위의 값을 swap해준다.
출처: https://www.crocus.co.kr/625 [Crocus]
"""



"""
7
1
5
2
10
-99
7
5
>
1
1
2
2
2
2
5
"""