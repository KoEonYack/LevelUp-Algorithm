"""
    @ Baek 11066 파일 합치기
    @ Prob. https://www.acmicpc.net/problem/11056
      Ref.  https://kunkunwoo.tistory.com/m/101?category=748892
    @ Algo: 
    @ Start day: 20. 09. 03.
    @ End day: 20. 09. 03.
"""

import sys

for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    # total = [0] * (501)
    # DP = [[0] * 501 for _ in range(501)]
    
    total = [0] * (N+1)
    DP = [[0] * (N+1) for _ in range(N+1)]
    
    
    for i in range(1, N+1):
        if i == 1:
            total[i] = arr[i]
        else:
            total[i] = total[i-1] + arr[i]
    
    
    for gap in range(1, N):
        
        start = 1
        while start + gap <= N:
            end = start + gap
            DP[start][end] = sys.maxsize
            
            mid = start
            while mid < end: 

                print("========")
                for d in DP:
                    print(d)
                
                DP[start][end] = min(DP[start][end], DP[start][mid] + DP[mid+1][end] + total[end] - total[start-1])
                mid += 1
                

                
            start += 1
    

    
    print(DP[1][N])

    
"""
1
4
40 30 30 50
>



2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
>
300
864
"""