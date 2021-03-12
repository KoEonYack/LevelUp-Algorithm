"""
    @ 1904. 01타일
    @ Prob. https://www.acmicpc.net/problem/1904
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 12.
    @ End day: 20. 01. 12.
"""


N = int(input())
arr = [0, 1, 2]
for i in range(3, N+1):
    num = arr[i-2] + arr[i-1]
    arr.append(num % 15746)

print(arr[N])


"""
1, 00

N=0 0   [0]
N=1 1  [1] 
N=2 00, 11 [2] 
N=3 001, 100, 111 [3] 
N=4 0011, 0000, 1001, 1100, 1111 [5] 
N=5 00 001, 00 1 00, 1 00 00,    [8]
    00 1 1 1, 1 00 1 1, 1 1 00 1, 1 1 1 00   
    1 1 1 1 1
    
4
>
5    
"""