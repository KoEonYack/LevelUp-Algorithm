"""
    @ Baek 10825 국영수
    @ Prob. https://www.acmicpc.net/problem/10825
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

arr = []

for i in range(int(input())):
    NAME, K, E, M = map(str, input().split())
    arr.append([NAME, int(K), int(E), int(M)])

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(len(arr)):
    print(arr[i][0])

"""
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
>
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
"""
