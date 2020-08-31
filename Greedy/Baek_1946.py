"""
    @ Baek 1946. 문서 검색
    @ Prob. https://www.acmicpc.net/problem/1946
     Ref.   
    @ Algo: Greedy 
    @ Start day: 20. 08. 27. 
    @ End day: 20. 08. 27.
"""


def solution(arr):
    ans = 0
    val = arr[0][1]
    
    # for a in arr:
    #     print(a)
        
    for i in range(len(arr)):
        if val >= arr[i][1]:
            ans += 1
            val = arr[i][1]
            
    return ans


for _ in range(int(input())):
    arr = []
    N = int(input())
    for _ in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
        
    arr.sort(key = lambda x: x[0])
    print(solution(arr))


"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
>
4
3

"""